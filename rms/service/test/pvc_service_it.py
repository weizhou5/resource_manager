import unittest
from unittest import mock
from unittest.mock import Mock, patch

from rms.client.mapper.storage_api import StorageClient
from rms.resource.resource import Resource
from rms.resource.rms import Rms
from rms.service.pvc_service import PvcService
from rms.service.test import BaseTestCase
from rms.swagger_server.models import Pvc


class PvcServiceTest(BaseTestCase):

    def setUp(self) -> None:
        self.pvc = Pvc(pvc_name='pvc_name',
                       disk=1,
                       namespace='namespace',
                       disk_type='file',
                       is_batch=True,
                       amount=1,
                       mode='RWX',
                       storage_class='ceph-fs-ssd',
                       module='modelDev')
        self.ou_id = 'ou_id'
        self.ou_name = 'ou_name'
        self.resource_api = Resource()
        self.namespace = 'test'
        self.pvc_name = 'test'

    @patch('rms.client.mapper.storage_api.StorageClient.insert')
    @patch('rms.resource.rms.Rms.create_pvc')
    def test_create_pvc(self, insert, create_pvc):
        insert.__enter__.return_value = True
        create_pvc.__enter__.return_value = 2
        try:
            pvc = PvcService.create_pvc(self.pvc, self.ou_id, self.ou_name)
            print(pvc)
        except Exception as e:
            print(e)

    @patch('rms.client.mapper.storage_api.StorageClient.delete')
    @patch('rms.resource.rms.Rms.delete_pvc')
    def test_delete_pvc(self, delete, delete_pvc):
        delete.__enter__.return_value = True
        delete_pvc.__enter__.return_value = 2
        try:
            pvc = PvcService.delete_pvc(self.namespace, [self.pvc_name], self.ou_id)
        except Exception as e:
            print(e)

    @patch('rms.client.mapper.storage_api.StorageClient.query')
    @patch('rms.resource.rms.Rms.check_pvc')
    def test_get_pvc(self, query, check_pvc):
        query.__enter__.return_value = True
        check_pvc.__enter__.return_value = 2
        try:
            pvc = PvcService.get_pvc(self.namespace, 'modelDev', self.ou_id)
        except Exception as e:
            print(e)

    @patch('rms.resource.rms.Rms.namespace_list')
    def test_get_pvc(self, namespace_list):
        namespace_list.__enter__.return_value = True
        try:
            pvc = PvcService.namespace_list(self.ou_id)
        except Exception as e:
            print(e)

    @patch('rms.resource.rms.Rms.get_mount')
    def test_get_mount(self, mount):
        mount.__enter__.return_value = True
        try:
            pvc = PvcService.namespace_list(self.namespace, ['test'])
        except Exception as e:
            print(e)
