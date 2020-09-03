#!/usr/bin/env python3
import base64
import os
import threading

from Crypto.Cipher import AES
import connexion
from sqlalchemy import create_engine

from rms import settings
from rms.AESEncrypt import AESEncrypt
from rms.client.k8s_conn_pool import K8sConnPoolSingleton
from rms.client.resource_conn_pool import ResourceConnPoolSingleton
from rms.client.storage_conn_pool import StorageConnPoolSingleton
from rms.metrics.metrics import health
from rms.route.metrics_route import metrics_blueprint
from rms.swagger_server import encoder
from rms.swagger_server.flask_error import ErrorHanlder
from rms.utils import flask_app_config, rms_config


def main():
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = connexion.App(__name__, specification_dir='rms/swagger_server/swagger', skip_error_handlers=True)
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config.from_object(settings.app_config[config_name])
    app_config = app.app.config
    app.app.register_blueprint(metrics_blueprint)
    # set errors
    ErrorHanlder.set_errors_handlers(app)

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
    StorageConnPoolSingleton(username=username, database=database, pw=pw, host=mysql_host, max_size=max_size,
                             max_usage=max_usage, idle=idle, ttl=ttl)
    ResourceConnPoolSingleton(resource_name=resource_name, max_size=max_size,
                              max_usage=max_usage, idle=idle, ttl=ttl)
    K8sConnPoolSingleton(max_size=max_size, max_usage=max_usage, idle=idle, ttl=ttl)
    # set route
    app.add_api('swagger.yaml', arguments={'title': 'resource manager API'})
    # start slo
    second = rms_config()["frequency_second"]
    timer = threading.Timer(second, health)
    timer.start()
    # run app
    app.run(host=app_config['HOST'], port=app_config['PORT'], debug=app_config['DEBUG'])


if __name__ == '__main__':
    main()
