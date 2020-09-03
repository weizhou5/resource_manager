import os

from rms.utils import flask_app_config



class BaseConfig(object):
    DEBUG = False
    HOST = flask_app_config()['host']
    PORT = 8080
    CONN_POOL_MAX_SIZE = 10
    CONN_POOL_MAX_USAGE = 100
    CONN_POOL_IDLE = 60
    CONN_POOL_TTL = 120
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'eap_rms')
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'root')
    MYSQL_PW = os.getenv('MYSQL_PW', 'root')
    MYSQL_HOST = os.getenv('MYSQL_HOST', '192.168.20.1')
    RESOURCE = os.getenv('RESOURCE', 'RMS')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'


class TestingConfig(BaseConfig):
    DEBUG = os.getenv('DEBUG', True)
    PORT = os.getenv('PORT', 5000)
    CONN_POOL_MAX_SIZE = os.getenv('CONN_POOL_MAX_SIZE', 10)
    CONN_POOL_MAX_USAGE = os.getenv('CONN_POOL_MAX_USAGE', 100)
    CONN_POOL_IDLE = os.getenv('CONN_POOL_IDLE', 60)
    CONN_POOL_TTL = os.getenv('CONN_POOL_TTL', 120)
    # github.com/jarus/flask-testing/issues/21
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
