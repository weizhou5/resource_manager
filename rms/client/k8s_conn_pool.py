from functools import wraps

from connection_pool import ConnectionPool
from kubernetes import config, client
from kubernetes.client.rest import ApiException
from kubernetes.config import ConfigException

from rms.common.exceptions import ServiceException


class K8sConnPoolSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls.create_pool(*args, **kwargs)
        return cls._instance

    @staticmethod
    def create_pool(max_size, max_usage, idle, ttl):

        def create_k8s_client():
            try:
                # Load configuration inside the Pod
                config.load_incluster_config()
            except ConfigException:
                # Load configuration for testing
                config.load_kube_config()

            # Create the Apis
            v1_core = client.CoreV1Api()
            return v1_core

        return ConnectionPool(create=create_k8s_client,
                              max_size=max_size,
                              max_usage=max_usage,
                              idle=idle,
                              ttl=ttl)


class k8s_conn_pool(object):
    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            with K8sConnPoolSingleton().item() as c:
                if 'service_api' not in kwargs:
                    kwargs['service_api'] = c
                try:
                    response = func(*args, **kwargs)
                except ApiException as e:
                    raise ServiceException(e.status, e.body, e.body)
                except Exception as e:
                    if isinstance(e, ServiceException):
                        raise e
                    else:
                        raise ServiceException(1000, e, '')
                return response

        return wrapped_function
