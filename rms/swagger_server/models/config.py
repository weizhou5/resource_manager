# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rms.swagger_server.models.config_detail import ConfigDetail
from rms.swagger_server.models.base_model_ import Model
from rms.swagger_server import util


class Config(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, module: ConfigDetail=None, storage_class: ConfigDetail=None, mode: ConfigDetail=None, disk_type: ConfigDetail=None):  # noqa: E501
        """Config - a entity defined in Swagger

        :param module: The module of this Config.  # noqa: E501
        :type module: ConfigDetail
        :param storage_class: The storage_class of this Config.  # noqa: E501
        :type storage_class: ConfigDetail
        :param mode: The mode of this Config.  # noqa: E501
        :type mode: ConfigDetail
        :param disk_type: The disk_type of this Config.  # noqa: E501
        :type disk_type: ConfigDetail
        """
        self.swagger_types = {
            'module': ConfigDetail,
            'storage_class': ConfigDetail,
            'mode': ConfigDetail,
            'disk_type': ConfigDetail
        }

        self.attribute_map = {
            'module': 'module',
            'storage_class': 'storage_class',
            'mode': 'mode',
            'disk_type': 'diskType'
        }

        self._module = module
        self._storage_class = storage_class
        self._mode = mode
        self._disk_type = disk_type

    @classmethod
    def from_dict(cls, dikt) -> 'Config':
        """Returns the dict as a entity

        :param dikt: A dict.
        :type: dict
        :return: The config of this Config.  # noqa: E501
        :rtype: Config
        """
        return util.deserialize_model(dikt, cls)

    @property
    def module(self) -> ConfigDetail:
        """Gets the module of this Config.


        :return: The module of this Config.
        :rtype: ConfigDetail
        """
        return self._module

    @module.setter
    def module(self, module: ConfigDetail):
        """Sets the module of this Config.


        :param module: The module of this Config.
        :type module: ConfigDetail
        """

        self._module = module

    @property
    def storage_class(self) -> ConfigDetail:
        """Gets the storage_class of this Config.


        :return: The storage_class of this Config.
        :rtype: ConfigDetail
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class: ConfigDetail):
        """Sets the storage_class of this Config.


        :param storage_class: The storage_class of this Config.
        :type storage_class: ConfigDetail
        """

        self._storage_class = storage_class

    @property
    def mode(self) -> ConfigDetail:
        """Gets the mode of this Config.


        :return: The mode of this Config.
        :rtype: ConfigDetail
        """
        return self._mode

    @mode.setter
    def mode(self, mode: ConfigDetail):
        """Sets the mode of this Config.


        :param mode: The mode of this Config.
        :type mode: ConfigDetail
        """

        self._mode = mode

    @property
    def disk_type(self) -> ConfigDetail:
        """Gets the disk_type of this Config.


        :return: The disk_type of this Config.
        :rtype: ConfigDetail
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type: ConfigDetail):
        """Sets the disk_type of this Config.


        :param disk_type: The disk_type of this Config.
        :type disk_type: ConfigDetail
        """

        self._disk_type = disk_type
