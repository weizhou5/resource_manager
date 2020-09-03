# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rms.swagger_server.models.base_model_ import Model
from rms.swagger_server import util


class Pvc(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pvc_name: str=None, disk: float=None, namespace: str=None, disk_type: str=None, is_batch: bool=None, amount: float=None, mode: str=None, storage_class: str=None, module: str=None):  # noqa: E501
        """Pvc - a model defined in Swagger

        :param pvc_name: The pvc_name of this Pvc.  # noqa: E501
        :type pvc_name: str
        :param disk: The disk of this Pvc.  # noqa: E501
        :type disk: float
        :param namespace: The namespace of this Pvc.  # noqa: E501
        :type namespace: str
        :param disk_type: The disk_type of this Pvc.  # noqa: E501
        :type disk_type: str
        :param is_batch: The is_batch of this Pvc.  # noqa: E501
        :type is_batch: bool
        :param amount: The amount of this Pvc.  # noqa: E501
        :type amount: float
        :param mode: The mode of this Pvc.  # noqa: E501
        :type mode: str
        :param storage_class: The storage_class of this Pvc.  # noqa: E501
        :type storage_class: str
        :param module: The module of this Pvc.  # noqa: E501
        :type module: str
        """
        self.swagger_types = {
            'pvc_name': str,
            'disk': float,
            'namespace': str,
            'disk_type': str,
            'is_batch': bool,
            'amount': float,
            'mode': str,
            'storage_class': str,
            'module': str
        }

        self.attribute_map = {
            'pvc_name': 'pvc_name',
            'disk': 'disk',
            'namespace': 'namespace',
            'disk_type': 'disk_type',
            'is_batch': 'is_batch',
            'amount': 'amount',
            'mode': 'mode',
            'storage_class': 'storage_class',
            'module': 'module'
        }

        self._pvc_name = pvc_name
        self._disk = disk
        self._namespace = namespace
        self._disk_type = disk_type
        self._is_batch = is_batch
        self._amount = amount
        self._mode = mode
        self._storage_class = storage_class
        self._module = module

    @classmethod
    def from_dict(cls, dikt) -> 'Pvc':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The pvc of this Pvc.  # noqa: E501
        :rtype: Pvc
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pvc_name(self) -> str:
        """Gets the pvc_name of this Pvc.

        pvc name.  # noqa: E501

        :return: The pvc_name of this Pvc.
        :rtype: str
        """
        return self._pvc_name

    @pvc_name.setter
    def pvc_name(self, pvc_name: str):
        """Sets the pvc_name of this Pvc.

        pvc name.  # noqa: E501

        :param pvc_name: The pvc_name of this Pvc.
        :type pvc_name: str
        """

        self._pvc_name = pvc_name

    @property
    def disk(self) -> float:
        """Gets the disk of this Pvc.

        disk capacity  # noqa: E501

        :return: The disk of this Pvc.
        :rtype: float
        """
        return self._disk

    @disk.setter
    def disk(self, disk: float):
        """Sets the disk of this Pvc.

        disk capacity  # noqa: E501

        :param disk: The disk of this Pvc.
        :type disk: float
        """

        self._disk = disk

    @property
    def namespace(self) -> str:
        """Gets the namespace of this Pvc.

        namespace.  # noqa: E501

        :return: The namespace of this Pvc.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this Pvc.

        namespace.  # noqa: E501

        :param namespace: The namespace of this Pvc.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def disk_type(self) -> str:
        """Gets the disk_type of this Pvc.


        :return: The disk_type of this Pvc.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type: str):
        """Sets the disk_type of this Pvc.


        :param disk_type: The disk_type of this Pvc.
        :type disk_type: str
        """

        self._disk_type = disk_type

    @property
    def is_batch(self) -> bool:
        """Gets the is_batch of this Pvc.

        true:pvc batch  create, false: pvc single create  # noqa: E501

        :return: The is_batch of this Pvc.
        :rtype: bool
        """
        return self._is_batch

    @is_batch.setter
    def is_batch(self, is_batch: bool):
        """Sets the is_batch of this Pvc.

        true:pvc batch  create, false: pvc single create  # noqa: E501

        :param is_batch: The is_batch of this Pvc.
        :type is_batch: bool
        """

        self._is_batch = is_batch

    @property
    def amount(self) -> float:
        """Gets the amount of this Pvc.

        acount  # noqa: E501

        :return: The amount of this Pvc.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this Pvc.

        acount  # noqa: E501

        :param amount: The amount of this Pvc.
        :type amount: float
        """

        self._amount = amount

    @property
    def mode(self) -> str:
        """Gets the mode of this Pvc.

        RWX  # noqa: E501

        :return: The mode of this Pvc.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        """Sets the mode of this Pvc.

        RWX  # noqa: E501

        :param mode: The mode of this Pvc.
        :type mode: str
        """

        self._mode = mode

    @property
    def storage_class(self) -> str:
        """Gets the storage_class of this Pvc.

        ceph-rbd-ssd  # noqa: E501

        :return: The storage_class of this Pvc.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class: str):
        """Sets the storage_class of this Pvc.

        ceph-rbd-ssd  # noqa: E501

        :param storage_class: The storage_class of this Pvc.
        :type storage_class: str
        """

        self._storage_class = storage_class

    @property
    def module(self) -> str:
        """Gets the module of this Pvc.

        modelDev  # noqa: E501

        :return: The module of this Pvc.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module: str):
        """Sets the module of this Pvc.

        modelDev  # noqa: E501

        :param module: The module of this Pvc.
        :type module: str
        """

        self._module = module