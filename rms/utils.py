# Logging
import json
import logging
import sys

import yaml


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def create_logger(name):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
    )
    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(logging.INFO)
    logger_instance.addHandler(handler)
    return logger_instance


logger = create_logger(__name__)

# read the first file that exists
RMS_CONFIG_PATHS = [
    'config/config.yaml',
]

FLASK_APP_CONFIG_PATHS = [
    '/etc/config/app_conf.yaml',
    './rms/config/app_conf.yaml',
    './config/app_conf.yaml',
    '../../config/app_conf.yaml'  # for integration test
]


def load_conf(paths):
    for config in paths:
        c = None
        try:
            with open(config, "r") as f:
                c = f.read()
        except IOError:
            continue

        try:
            if yaml.safe_load(c) is None:
                # YAML exists but is empty
                return {}
            else:
                # YAML exists and is not empty
                return yaml.safe_load(c)
        except yaml.YAMLError:
            logger.error("pipeline config is not a valid yaml")
            return {}
        except AttributeError as e:
            logger.error(
                "Can't load the config at {}: {}".format(config, str(e))
            )

    logger.warning("Couldn't load any config")
    return {}


def rms_config():
    return load_conf(RMS_CONFIG_PATHS)


def flask_app_config():
    return load_conf(FLASK_APP_CONFIG_PATHS)


def load_param_yaml(f, **kwargs):
    c = None
    try:
        with open(f, "r") as f:
            c = f.read().format(**kwargs)
    except IOError:
        logger.info("Error opening: {}".format(f))
        return None

    try:
        if yaml.safe_load(c) is None:
            # YAML exists but is empty
            return {}
        else:
            # YAML exists and is not empty
            return yaml.safe_load(c)
    except yaml.YAMLError as e:
        logger.warning("Couldn't load yaml: {}".format(e))
        return None
