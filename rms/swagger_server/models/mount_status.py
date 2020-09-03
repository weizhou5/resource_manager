# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rms.swagger_server.models.base_model_ import Model
from rms.swagger_server import util


class MountStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, namespace: str=None, name: str=None, usage: List[str]=None):  # noqa: E501
        """MountStatus - a model defined in Swagger

        :param namespace: The namespace of this MountStatus.  # noqa: E501
        :type namespace: str
        :param name: The name of this MountStatus.  # noqa: E501
        :type name: str
        :param usage: The usage of this MountStatus.  # noqa: E501
        :type usage: List[str]
        """
        self.swagger_types = {
            'namespace': str,
            'name': str,
            'usage': List[str]
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'name': 'name',
            'usage': 'usage'
        }

        self._namespace = namespace
        self._name = name
        self._usage = usage

    @classmethod
    def from_dict(cls, dikt) -> 'MountStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The mountStatus of this MountStatus.  # noqa: E501
        :rtype: MountStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def namespace(self) -> str:
        """Gets the namespace of this MountStatus.


        :return: The namespace of this MountStatus.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this MountStatus.


        :param namespace: The namespace of this MountStatus.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def name(self) -> str:
        """Gets the name of this MountStatus.


        :return: The name of this MountStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this MountStatus.


        :param name: The name of this MountStatus.
        :type name: str
        """

        self._name = name

    @property
    def usage(self) -> List[str]:
        """Gets the usage of this MountStatus.

        pvc mount module  # noqa: E501

        :return: The usage of this MountStatus.
        :rtype: List[str]
        """
        return self._usage

    @usage.setter
    def usage(self, usage: List[str]):
        """Sets the usage of this MountStatus.

        pvc mount module  # noqa: E501

        :param usage: The usage of this MountStatus.
        :type usage: List[str]
        """

        self._usage = usage
