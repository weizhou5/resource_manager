from functools import wraps
from connection_pool import ConnectionPool
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from rms.client.entity.rms_pvc import Base
from rms.common.exceptions import ServiceException


class StorageConnPoolSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls.create_pool(*args, **kwargs)
        return cls._instance

    @staticmethod
    def create_pool(username, pw, host, database, max_size, max_usage, idle, ttl):
        def create_storage_client():
            engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format(username, pw, host, database))
            if not database_exists(engine.url):
                create_database(engine.url)
            Base.metadata.create_all(engine)
            return engine

        return ConnectionPool(create=create_storage_client,
                              max_size=max_size,
                              max_usage=max_usage,
                              idle=idle,
                              ttl=ttl)


class StorageConnectPool(object):
    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            with StorageConnPoolSingleton().item() as c:
                if 'service_api' not in kwargs:
                    kwargs['service_api'] = c
                try:
                    response = func(*args, **kwargs)
                except Exception as e:
                    if isinstance(e, ServiceException):
                        raise e
                    else:
                        raise ServiceException(1000, e, '')
                return response

        return wrapped_function
