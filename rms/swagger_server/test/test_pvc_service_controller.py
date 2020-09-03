# coding: utf-8

from __future__ import absolute_import

from unittest import mock
from unittest.mock import Mock

from flask import json

from rms.client.resource_conn_pool import ResourceConnPoolSingleton, ResourceConnectPool
from rms.resource.resource import Resource
from rms.resource.rms import Rms
from rms.service.pvc_service import PvcService
from rms.swagger_server.models import PvcDetail
from rms.swagger_server.models.pvc import Pvc  # noqa: E501
from rms.swagger_server.test import BaseTestCase


# from rms.resource.resource import Resource


class TestPvcServiceController(BaseTestCase):
    """PvcServiceController integration test stubs"""

    def setUp(self) -> None:
        self.headers = \
            {
                "X-Member-Id": "23832170000",
                "X-Region": "1100000",
                "X-Channel": "01",
                "Content-Type": "application/json;charset=UTF-8",
                "eap-user": "50nV0PlZYHD+OyUzTwZmHRVVPxEO0hr+CuoUIm8tnU+QKhZr9CTOhK5pgmMU/b2nfUYKaFJftkMOgOliXB8B0IKG0VMrwDq7TGHWzKp7VavV5macA614ptDkeX5qVS1y72nHIHBNZRRYux/aiTuyM1oGHBF+NHi6JL/jCcvmU4n+yms5MUbwTCMJ0oioQlE+eJtDdpjMy4qtaXohetS0/p9UgpLcK7nEPlaQO6ipmtIFGqxj2cfma83KaK14u3evQydy4NsP6FyOZsjqQabwWo0kgwZiXAFuKGYmrgBja4ANMg2ykQRVkzS4/o8x8Bi7H5rdlaF55Rb8rv9jKSNiwb+DtULkWfgcSG6r4UMzWXYovy+r+geJJjbyjWIKkjoBpAnByIOynhQViBrp00MpnFD/RZUCJFFouwDIy5lb8+blZmcLilOz8BduXBb5vZIfY8po2VJDMWbPJ/DQJvWAtKxGvZ9ekehTPf0nEkjFg7popo5BmkKQ8KdGmPPNDNL8tOL9p/OshFkHV+E7nmbzh6lLJBEXMTkOhfGEhkxvryNlKJo2f99TEdESVqoOFDU9m+w2HV7WqWki+9dNJR2dzff/TLrMV2uxVSBU/qPZGpv/yshDkhuq4dCO7P0axUv7T3+lRAKtHa77W7t02924t2O8EMmXHyoLaCvb1b5/u+yapbMD/UoLKx5kHEhMaqNMRfSfr20XJdw8SYQvafsaTnbF5z9qtdzVO/AjMaqLbl+JkERR9QraERAfh+U3gamlI15T4n5WTBRIUwAeu4itF/r97LFIidHDzNLBjgkW0qh3aWb6OrxxOdrSaA/rxFrgjmsQBDtlPp/SmMoIt8ic4POOOKr3h1CVozOr3bEn4iPKyK3ud2UVwz87Q7ZcgDLtoY0sBKTcwIkQS9VIkF+kKaDwpmZ9KR2b7D5whqAifGIjcv9yIVwNcf6AYqDl9z/bTPMoWP6WUuTpf/aTaie1QiMZOV0CmdJ4lzhrdh5DhAXuNKdjCi2HiPJwKIoonWxklMcAb9y+x8hzmH/kkcCdiWbiKVNWWkLTvbQ5MKo55Adm9OfRYMWgXj2m6lSTcBQB"
            }
        self.pvc = PvcDetail(pvc_name='name',
                             disk=1,
                             namespace='namespace',
                             disk_type='disk_type',
                             mode='mode',
                             storage_class='storage_class',
                             module='modelDev',
                             user='ou_name',
                             create_date=1000)
        self.mount = {'mount': ['test']}

    def test_create_pvc(self):
        """Test case for create_pvc

        Create a pvc.
        """
        PvcService.create_pvc = Mock(return_value=['test'])
        body = Pvc()
        response = self.client.open(
            '/apis/v1beta1/pvc',
            method='POST',
            headers=self.headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pvc(self):
        """Test case for delete_pvc

        delete pvc.
        """
        PvcService.delete_pvc = Mock(return_value=['name_example'])
        query_string = [('namespace', 'namespace_example'),
                        ('pvc_name', 'name_example')]
        response = self.client.open(
            '/apis/v1beta1/pvc/namespace/{namespace}'.format(namespace='namespace_example'),
            method='DELETE',
            headers=self.headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pvc_mount(self):
        """Test case for get_pvc_mount

        check pvc.
        """
        query_string = [('namespace', 'namespace_example'),
                        ('pvc_name', 'name_example')]
        PvcService.get_pvc_mount = Mock(return_value=self.mount)
        response = self.client.open(
            '/apis/v1beta1/pvc/mount',
            method='GET',
            headers=self.headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_pvc(self):
        """Test case for list_pvc

        Find all pvc under the namespace or ou.
        """
        PvcService.get_pvc = Mock(return_value=self.pvc)
        query_string = [('namespace', 'namespace_example'),
                        ('module', 'module_example')]
        response = self.client.open(
            '/apis/v1beta1/pvc',
            method='GET',
            headers=self.headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_namespace_list(self):
        """Test case for namespace_list

        namespace list
        """
        PvcService.namespace_list = Mock(return_value=['test'])
        response = self.client.open(
            '/apis/v1beta1/namespace',
            method='GET',
            headers=self.headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
