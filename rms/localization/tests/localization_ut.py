import unittest

from rms.client.minio_api_component import equal_groups, merge_groups
from rms.localization.localization import localize, Locale


class TestLocalization(unittest.TestCase):
    def test_localization(self):
        name = localize('filesource', Locale.ZH)
        assert name == '文件'
