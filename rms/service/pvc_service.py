import os
import time
from datetime import datetime
from kubernetes import client, config
from rms.client.mapper.storage_api import StorageClient
from rms.client.entity.rms_pvc import RmsPvc
from rms.client.resource_conn_pool import ResourceConnectPool
from rms.common.exceptions import ServiceException
from rms.metrics.metrics import metrics_summary
from rms.resource.resource import Resource
from rms.service.msg import Msg
from rms.swagger_server.models import PvcDetail, pvc_status
from rms.swagger_server.models.pvc_status import PvcStatus
from rms.utils import rms_config

PVC_DELETE_SUCCESS = 2
PVC_DELETED = 4
PVC_CREATE_SUCCESS = 2
SUCCESS = 'success'
label = "pvc create"


class PvcService(object):
    @staticmethod
    @ResourceConnectPool()
    def create_pvc(pvc, ou_id, ou_name, resource_api: Resource = None):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = []
            if pvc.amount is None or pvc.amount < 1:
                raise ServiceException(Msg['AMOUNT_ERROR'])
            amount = int(pvc.amount)
            tmp_name = pvc.pvc_name
            for i in range(amount):
                if amount > 1:
                    pvc_name_tmp = tmp_name + '-' + str(i)
                else:
                    pvc_name_tmp = tmp_name
                rms_pvc_tmp = RmsPvc(name=pvc_name_tmp,
                                     namespace=pvc.namespace,
                                     capacity=pvc.disk,
                                     disk_type=pvc.disk_type,
                                     mode=pvc.mode,
                                     storage_class=pvc.storage_class,
                                     module=pvc.module,
                                     is_delete=0,
                                     ou_id=ou_id,
                                     ou_name=ou_name,
                                     cre_user=ou_id,
                                     cre_date=timestamp, upd_user=ou_id, upd_date=timestamp)
                with StorageClient.insert(rms_pvc_tmp):
                    pvc.pvc_name = rms_pvc_tmp.name
                    code = resource_api.create_pvc(body=pvc)
                    status = PvcStatus()
                    status.namespace = rms_pvc_tmp.namespace
                    status.name = rms_pvc_tmp.name
                    if code == PVC_CREATE_SUCCESS:
                        status.status = True
                        status.message = SUCCESS
                        data.append(status)
                        metrics_summary(label=label, count=1)
                    else:
                        metrics_summary(label=label, count=0)
                        status.status = False
                        status.message = code
                        data.append(status)
                        raise ServiceException(Msg['CREATE_PVC_ERROR'])
            return data
        except Exception as e:
            metrics_summary(label=label, count=0)
            raise e

    @staticmethod
    @ResourceConnectPool()
    def delete_pvc(namespace, pvc_list, ou_id, resource_api: Resource = None):
        data = []
        for pvc_name in pvc_list:
            with StorageClient.delete(namespace=namespace,
                                      pvc_name=pvc_name,
                                      ou_id=ou_id):
                pvc_delete_status = PvcStatus()
                pvc_delete_status.namespace = namespace
                pvc_delete_status.name = pvc_name
                status = resource_api.delete_pvc(namespace, pvc_name)
                if status == PVC_DELETE_SUCCESS:
                    pvc_delete_status.status = True
                    pvc_delete_status.message = SUCCESS
                    data.append(pvc_delete_status)
                else:
                    pvc_delete_status.status = False
                    pvc_delete_status.message = status
                    data.append(pvc_delete_status)
                    raise ServiceException(Msg['DELETE_ERROR'])
        return data

    @staticmethod
    @ResourceConnectPool()
    def get_pvc(storage_type, namespace, module, ou_id, resource_api: Resource = None):
        data = []
        if storage_type == 'notebook' and resource_api.check_key_tab(namespace=namespace, ou_id=ou_id) is True:
            key_tab_pvc = rms_config()["keytab"]
            for pvc in key_tab_pvc:
                detail = PvcDetail(pvc_name=pvc, namespace=namespace, create_date=int(time.time()) * 1000)
                data.append(detail)
        elif namespace is not None:
            rows = StorageClient.query(namespace=namespace, module=module, ou_id=ou_id)
            for row in rows:
                if resource_api.check_pvc(row['namespace'], row['name']):
                    data.append(PvcService.transform_pvc(row))
        return data

    @staticmethod
    @ResourceConnectPool()
    def namespace_list(ou_id, resource_api: Resource = None):
        namespace_list = resource_api.namespace_list(ou_id)
        default_namespace = os.getenv('DEFAULT_NAMESPACE', '')
        namespaces = [default_namespace]
        for namespace in namespace_list:
            if namespace not in namespaces:
                namespaces.append(namespace)
        return namespaces

    @staticmethod
    @ResourceConnectPool()
    def get_pvc_mount(namespace, pvc_list, resource_api: Resource = None):
        pvc_mount = resource_api.get_mount(namespace)
        mount = {}
        for pvc in pvc_list:
            if pvc in pvc_mount:
                mount[pvc] = pvc_mount[pvc]
        return mount

    @staticmethod
    def transform_pvc(row):
        return PvcDetail(pvc_name=row['name'],
                         disk=row['capacity'],
                         namespace=row['namespace'],
                         disk_type=row['disk_type'],
                         mode=row['mode'],
                         storage_class=row['storage_class'],
                         module=row['module'],
                         user=row['ou_name'],
                         create_date=int(datetime.strptime(row['cre_date'], '%Y-%m-%d %H:%M:%S').timestamp() * 1000))
