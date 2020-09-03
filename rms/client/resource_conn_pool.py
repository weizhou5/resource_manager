from functools import wraps
from connection_pool import ConnectionPool
from rms.common.exceptions import ServiceException
from rms.resource.resource_enum import ResourceEnum


class ResourceConnPoolSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls.create_pool(*args, **kwargs)
        return cls._instance

    @staticmethod
    def create_pool(resource_name, max_size, max_usage, idle, ttl):
        def create_resource_client():
            resource = ResourceEnum[resource_name].value
            return resource

        return ConnectionPool(create=create_resource_client,
                              max_size=max_size,
                              max_usage=max_usage,
                              idle=idle,
                              ttl=ttl)


class ResourceConnectPool(object):
    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            with ResourceConnPoolSingleton().item() as c:
                if 'resource_api' not in kwargs:
                    kwargs['resource_api'] = c
                try:
                    response = func(*args, **kwargs)
                except Exception as e:
                    if isinstance(e, ServiceException):
                        raise e
                    else:
                        raise ServiceException(1000, e, '')
                return response

        return wrapped_function
