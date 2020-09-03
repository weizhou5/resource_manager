import kubernetes
from kubernetes.client import CoreV1Api

from rms.client.k8s_conn_pool import k8s_conn_pool
from rms.resource.resource import Resource
from rms.utils import rms_config, load_param_yaml, logger

PVC_TEMPLATE = "rms/common/yaml/pvc.yaml"


class K8s(Resource):
    def check_key_tab(self, namespace, ou_id):
        return True

    @k8s_conn_pool()
    def get_mount(self, namespace, service_api: CoreV1Api = None):
        pvc_mount = {}
        pods = service_api.list_namespaced_pod(namespace, watch=False)
        for pod in pods.items:
            phase = pod.status.phase
            if pod.status.phase != 'Succeeded':
                for v in pod.spec.volumes:
                    if v.persistent_volume_claim:
                        if v.persistent_volume_claim.claim_name in pvc_mount:
                            pvc_mount[v.persistent_volume_claim.claim_name].append(pod.metadata.name)
                        else:
                            install = [pod.metadata.name]
                            pvc_mount[v.persistent_volume_claim.claim_name] = install
        return pvc_mount

    def namespace_list(self, ou_id):
        data = rms_config()["namespace"]
        return data

    @k8s_conn_pool()
    def create_pvc(self, body, service_api: CoreV1Api = None):
        pvc = load_param_yaml(PVC_TEMPLATE,
                              name=body.pvc_name,
                              namespace=body.namespace,
                              #accessModes="ReadWriteMany" if body.mode == "RWX" else "ReadWriteOnce",
                              accessModes=body.mode,
                              storage=body.disk,
                              storageClassName=body.storage_class
                              )
        try:
            service_api.create_namespaced_persistent_volume_claim(body.namespace, body=pvc)
        except Exception as e:
            logger.error(e)
            return -1
        return 2

    @k8s_conn_pool()
    def delete_pvc(self, namespace, name, service_api: CoreV1Api = None):
        try:
            service_api.delete_namespaced_persistent_volume_claim(name, namespace)
        except Exception as e:
            logger.error(e)
            return -1
        return 2

    @k8s_conn_pool()
    def check_pvc(self, namespace, name, service_api: CoreV1Api = None):
        try:
            claim = service_api.read_namespaced_persistent_volume_claim(name, namespace)
        except Exception as e:
            logger.error(e)
            return False
        return True
