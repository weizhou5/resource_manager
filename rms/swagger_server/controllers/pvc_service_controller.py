import json

import connexion

import configparser
from rms.service.pvc_service import PvcService
from rms.swagger_server import util
from rms.swagger_server.models import ApiStatus
from rms.swagger_server.models.pvc import Pvc
from rms.utils import flask_app_config, rms_config


def create_pvc(body):  # noqa: E501
    """Create a pvc.

     # noqa: E501

        :param body:
            :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        pvc = Pvc.from_dict(connexion.request.get_json())  # noqa: E501
        ou_name = util.get_user(request=connexion.request)
        ou_id = util.get_ou_id(request=connexion.request)
        data = PvcService.create_pvc(pvc=pvc, ou_id=ou_id, ou_name=ou_name)
        return ApiStatus(code=0, msg='success', data=data)


def delete_pvc(namespace, pvc_name):  # noqa: E501
    """Create a pvc.

     # noqa: E501

        :param namespace:
                :type namespace: str
        :param pvc_name:
                    :type pvc_name: List[str]

    :rtype: None
    """
    ou_id = util.get_ou_id(request=connexion.request)
    data = PvcService.delete_pvc(namespace=namespace, pvc_list=pvc_name, ou_id=ou_id)
    return ApiStatus(code=0, msg='success', data=data)


def get_config():  # noqa: E501
    """Get config.

     # noqa: E501


    :rtype: object
    """
    data = rms_config()["ui"]
    return ApiStatus(code=0, msg='success', data=data)


def list_pvc(storage_type=None, namespace=None, module=None):  # noqa: E501
    """Find all pvc under the namespace or ou.

     # noqa: E501

        :param storage_type:
        :param namespace:
                :type namespace: str
        :param module:
                    :type module: List[str]

    :rtype: object
    """
    ou_id = util.get_ou_id(request=connexion.request)
    rows = PvcService.get_pvc(storage_type=storage_type, namespace=namespace, module=module, ou_id=ou_id)
    return ApiStatus(code=0, msg='success', data=rows)


def get_pvc_mount(namespace, pvc_name):  # noqa: E501
    """Get config.

     # noqa: E501

        :param pvc_name:
        :param namespace:
                :type namespace: str
        :param name:
                :type name: str

    :rtype: object
    """
    data = PvcService.get_pvc_mount(namespace=namespace, pvc_list=pvc_name)
    return ApiStatus(code=0, msg='success', data=data)

