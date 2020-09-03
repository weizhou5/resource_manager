# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rms.swagger_server.models.base_model_ import Model
from rms.swagger_server import util


class PvcDetail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pvc_name: str=None, disk: float=None, namespace: str=None, disk_type: str=None, mode: str=None, storage_class: str=None, module: str=None, user: str=None, create_date: str=None):  # noqa: E501
        """PvcDetail - a entity defined in Swagger

        :param pvc_name: The pvc_name of this PvcDetail.  # noqa: E501
        :type pvc_name: str
        :param disk: The disk of this PvcDetail.  # noqa: E501
        :type disk: float
        :param namespace: The namespace of this PvcDetail.  # noqa: E501
        :type namespace: str
        :param disk_type: The disk_type of this PvcDetail.  # noqa: E501
        :type disk_type: str
        :param mode: The mode of this PvcDetail.  # noqa: E501
        :type mode: str
        :param storage_class: The storage_class of this PvcDetail.  # noqa: E501
        :type storage_class: str
        :param module: The module of this PvcDetail.  # noqa: E501
        :type module: str
        :param user: The user of this PvcDetail.  # noqa: E501
        :type user: str
        :param create_date: The create_date of this PvcDetail.  # noqa: E501
        :type create_date: str
        """
        self.swagger_types = {
            'pvc_name': str,
            'disk': float,
            'namespace': str,
            'disk_type': str,
            'mode': str,
            'storage_class': str,
            'module': str,
            'user': str,
            'create_date': str
        }

        self.attribute_map = {
            'pvc_name': 'pvc_name',
            'disk': 'disk',
            'namespace': 'namespace',
            'disk_type': 'disk_type',
            'mode': 'mode',
            'storage_class': 'storage_class',
            'module': 'module',
            'user': 'user',
            'create_date': 'create_date'
        }

        self._pvc_name = pvc_name
        self._disk = disk
        self._namespace = namespace
        self._disk_type = disk_type
        self._mode = mode
        self._storage_class = storage_class
        self._module = module
        self._user = user
        self._create_date = create_date

    @classmethod
    def from_dict(cls, dikt) -> 'PvcDetail':
        """Returns the dict as a entity

        :param dikt: A dict.
        :type: dict
        :return: The pvcDetail of this PvcDetail.  # noqa: E501
        :rtype: PvcDetail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pvc_name(self) -> str:
        """Gets the pvc_name of this PvcDetail.

        pvc name.  # noqa: E501

        :return: The pvc_name of this PvcDetail.
        :rtype: str
        """
        return self._pvc_name

    @pvc_name.setter
    def pvc_name(self, pvc_name: str):
        """Sets the pvc_name of this PvcDetail.

        pvc name.  # noqa: E501

        :param pvc_name: The pvc_name of this PvcDetail.
        :type pvc_name: str
        """

        self._pvc_name = pvc_name

    @property
    def disk(self) -> float:
        """Gets the disk of this PvcDetail.

        disk capacity  # noqa: E501

        :return: The disk of this PvcDetail.
        :rtype: float
        """
        return self._disk

    @disk.setter
    def disk(self, disk: float):
        """Sets the disk of this PvcDetail.

        disk capacity  # noqa: E501

        :param disk: The disk of this PvcDetail.
        :type disk: float
        """

        self._disk = disk

    @property
    def namespace(self) -> str:
        """Gets the namespace of this PvcDetail.

        namespace.  # noqa: E501

        :return: The namespace of this PvcDetail.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this PvcDetail.

        namespace.  # noqa: E501

        :param namespace: The namespace of this PvcDetail.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def disk_type(self) -> str:
        """Gets the disk_type of this PvcDetail.


        :return: The disk_type of this PvcDetail.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type: str):
        """Sets the disk_type of this PvcDetail.


        :param disk_type: The disk_type of this PvcDetail.
        :type disk_type: str
        """

        self._disk_type = disk_type

    @property
    def mode(self) -> str:
        """Gets the mode of this PvcDetail.

        RWX  # noqa: E501

        :return: The mode of this PvcDetail.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        """Sets the mode of this PvcDetail.

        RWX  # noqa: E501

        :param mode: The mode of this PvcDetail.
        :type mode: str
        """

        self._mode = mode

    @property
    def storage_class(self) -> str:
        """Gets the storage_class of this PvcDetail.

        ceph-rbd-ssd  # noqa: E501

        :return: The storage_class of this PvcDetail.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class: str):
        """Sets the storage_class of this PvcDetail.

        ceph-rbd-ssd  # noqa: E501

        :param storage_class: The storage_class of this PvcDetail.
        :type storage_class: str
        """

        self._storage_class = storage_class

    @property
    def module(self) -> str:
        """Gets the module of this PvcDetail.

        apply to module  # noqa: E501

        :return: The module of this PvcDetail.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module: str):
        """Sets the module of this PvcDetail.

        apply to module  # noqa: E501

        :param module: The module of this PvcDetail.
        :type module: str
        """

        self._module = module

    @property
    def user(self) -> str:
        """Gets the user of this PvcDetail.


        :return: The user of this PvcDetail.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this PvcDetail.


        :param user: The user of this PvcDetail.
        :type user: str
        """

        self._user = user

    @property
    def create_date(self) -> str:
        """Gets the create_date of this PvcDetail.


        :return: The create_date of this PvcDetail.
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: str):
        """Sets the create_date of this PvcDetail.


        :param create_date: The create_date of this PvcDetail.
        :type create_date: str
        """

        self._create_date = create_date