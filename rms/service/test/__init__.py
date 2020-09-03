import logging
import os
from unittest.mock import Mock

import connexion
from flask_testing import TestCase
from sqlalchemy import create_engine

from rms import settings
from rms.client.k8s_conn_pool import K8sConnPoolSingleton
from rms.client.resource_conn_pool import ResourceConnPoolSingleton
from rms.client.storage_conn_pool import StorageConnPoolSingleton
from rms.resource.rms import Rms
from rms.swagger_server import encoder
from rms.swagger_server.flask_error import ErrorHanlder


class BaseTestCase(TestCase):

    def create_app(self):
        config_name = os.getenv('FLASK_CONFIG', 'testing')
        app = connexion.App(__name__, specification_dir='./rms/swagger_server/swagger', skip_error_handlers=True)
        app.app.json_encoder = encoder.JSONEncoder
        app.app.config.from_object(settings.app_config[config_name])
        app_config = app.app.config
        # set errors
        ErrorHanlder.set_errors_handlers(app)

        # init kfp connection pool
        # init connection pool
        max_size = app_config['CONN_POOL_MAX_SIZE']
        max_usage = app_config['CONN_POOL_MAX_USAGE']
        idle = app_config['CONN_POOL_IDLE']
        ttl = app_config['CONN_POOL_TTL']
        username = app_config['MYSQL_USERNAME']
        database = app_config['MYSQL_DATABASE']
        pw = app_config['MYSQL_PW']
        mysql_host = app_config['MYSQL_HOST']
        resource_name = app_config['RESOURCE']
        StorageConnPoolSingleton.create_pool = Mock(return_value=[])
        StorageConnPoolSingleton(username=username, database=database, pw=pw, host=mysql_host, max_size=max_size,
                                 max_usage=max_usage, idle=idle, ttl=ttl)
        ResourceConnPoolSingleton(resource_name=resource_name, max_size=1,
                                  max_usage=1, idle=idle, ttl=ttl)
        K8sConnPoolSingleton(max_size=max_size, max_usage=max_usage, idle=idle, ttl=ttl)
        # run app
        return app.app
