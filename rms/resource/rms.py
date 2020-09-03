import json
import os

from kubernetes.client import CoreV1Api

from rms import utils
from rms.client.k8s_conn_pool import k8s_conn_pool
from rms.resource.resource import Resource
import requests
from kubernetes import client, config

from rms.swagger_server.models.namespace_status import NamespaceStatus
from rms.swagger_server.models.resource_status import ResourceStatus
from rms.utils import logger, rms_config

SUCCESS = 0

URI = '/pvc'


class Rms(Resource):
    def namespace_list(self, ou_id):
        resource_host = os.getenv('RMS_CU_HOST', 'http://eap-rms-cu.alpha-k8s-cn4.eniot.io')
        resource_uri = os.getenv('RMS_CU_URI', '/rms/usage')
        host = '{}{}'.format(resource_host, resource_uri)
        params = {'ouId': ou_id}
        response = requests.get(host, params=params)
        data_array = response.json()['data']
        namespace = []
        for resource in data_array:
            namespace.append(resource['namespace'])
        return namespace

    url = ''

    def __init__(self):
        url = ''

    def create_pvc(self, body):
        params = {'quota': body.disk, 'pvcName': body.pvc_name, 'namespace': body.namespace,
                  'diskType': body.storage_class}
        headers = \
            {
                "X-Member-Id": "23832170000",
                "X-Region": "1100000",
                "X-Channel": "01",
                "Content-Type": "application/json;charset=UTF-8"
            }
        response = requests.post(self.get_rms_url() + URI, headers=headers, data=json.dumps(params))
        if 'code' in response.json():
            logger.info(response.text)
            code = int(response.json()['code'])
            if code == 2:
                return code
            else:
                return response.json()['message']
        else:
            return -1

    def delete_pvc(self, namespace, name):
        params = {'namespace': namespace, 'pvcName': name}
        response = requests.delete(self.get_rms_url() + URI, params=params)
        if 'code' in response.json():
            code = int(response.json()['code'])
            if code == 2:
                return code
            else:
                return response.json()['message']
        else:
            return -1

    def get_rms_url(self):
        resource_host = os.getenv('RMS_HOST', 'http://rms-server.alpha-k8s-cn4.eniot.io')
        resource_uri = os.getenv('RMS_URI', '/api/v1/kubernetes')
        return '{}{}'.format(resource_host, resource_uri)

    def get_rm_url(self):
        resource_host = os.getenv('RM_HOST', 'http://rm-service.alpha-k8s-cn4.eniot.io')
        resource_uri = os.getenv('RM_URI', '/rm/resource/query/detail')
        return '{}{}'.format(resource_host, resource_uri)

    def check_pvc(self, namespace, ou_id):
        return True

    def check_key_tab(self, namespace, ou_id):
        if namespace is None or ou_id is None:
            return False
        service_name = os.getenv("SERVICE_NAME", "ml_model_container")
        ou_id = os.getenv("OU_ID")
        url = '{}?ouId={}&serviceName={}'.format(self.get_rm_url(), ou_id, service_name)
        response = requests.get(url)
        dumps = json.loads(response.text)
        for data in dumps['data']:
            resource_detail = ResourceStatus()
            resource_detail.__dict__.update(data)
            if resource_detail.taskParameters is not None:
                namespace_status = NamespaceStatus()
                namespace_status.__dict__.update(resource_detail.taskParameters['namespace'])
                if namespace_status.hasKeytab == 'true' and namespace_status.namespaceName == namespace:
                    return True
        return False

    @k8s_conn_pool()
    def get_mount(self, namespace, service_api: CoreV1Api = None):
        pvc_mount = {}
        # pods = service_api.list_namespaced_pod(namespace, watch=False)
        # for pod in pods.items:
        #     phase = pod.status.phase
        #     if pod.status.phase != 'Succeeded':
        #         for v in pod.spec.volumes:
        #             if v.persistent_volume_claim:
        #                 if v.persistent_volume_claim.claim_name in pvc_mount:
        #                     pvc_mount[v.persistent_volume_claim.claim_name].append(pod.metadata.name)
        #                 else:
        #                     install = [pod.metadata.name]
        #                     pvc_mount[v.persistent_volume_claim.claim_name] = install
        return pvc_mount
