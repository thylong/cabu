# -*- coding: utf-8 -*-

import os
import unittest
from cabu import Cabu
import json


from mock import patch, MagicMock


class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBase, self).__init__(*args, **kwargs)

        self.patcher_xvfb = patch('cabu.drivers.Xvfb', spec=True)
        self.patcher_xvfb.start()
        self.patcher_ftpretty = patch('cabu.core.ftpretty', spec=True)
        self.patcher_ftpretty.start()

    def __del__(self, *args, **kwargs):
        self.patcher_ftpretty.stop()
        self.patcher_xvfb.stop()

    def __exit__(self, *args, **kwargs):
        self.patcher_ftpretty.stop()
        self.patcher_xvfb.stop()
        super(TestBase, self).__exit__(*args, **kwargs)

    @patch('cabu.drivers.load_phantomjs', return_value=MagicMock())
    def setUp(self, mock_driver):
        if 'CABU_SETTINGS' in os.environ:
            del os.environ['CABU_SETTINGS']
        os.environ['CABU_SETTINGS'] = 'cabu.tests.test_settings'
        self.app = Cabu(__name__)
        self.config = self.app.config
        self.vdisplay = self.app.vdisplay
        self.client = self.app.test_client()

    def tearDown(self):
        if hasattr(self, 'ftp'):
            self.ftp.close()
        if 'CABU_SETTINGS' in os.environ:
            del os.environ['CABU_SETTINGS']
        if hasattr(self, 'app'):
            del self.app

    def get(self, resource, item=None, query='', headers=[]):
        url = self.resolve_resource(resource, item)
        res = self.client.get(url + query, headers=headers)
        return self.parse_response(res)

    def post(self, resource, data, item=None, headers=[], content_type=None):
        if not content_type:
            content_type = 'application/json'
        headers.append(('Content-Type', content_type))
        url = self.resolve_resource(resource, item)
        res = self.client.post(url, data=json.dumps(data), headers=headers)
        return self.parse_response(res)

    def put(self, resource, data, item=None, headers=[]):
        headers.append(('Content-Type', 'application/json'))
        url = self.resolve_resource(resource, item)
        res = self.client.put(url, data=json.dumps(data), headers=headers)
        return self.parse_response(res)

    def patch(self, resource, data, item=None, headers=[]):
        headers.append(('Content-Type', 'application/json'))
        url = self.resolve_resource(resource, item)
        res = self.client.patch(url, data=json.dumps(data), headers=headers)
        return self.parse_response(res)

    def delete(self, resource, item=None, headers=None):
        url = self.resolve_resource(resource, item)
        res = self.client.delete(url, headers=headers)
        return self.parse_response(res)

    def parse_response(self, res):
        val = None
        if res.get_data():
            val = res.get_data().decode("utf-8")
            try:
                val = json.loads(val)
            except ValueError:
                self.fail("'%s' is not valid JSON" % (val))

        return val, res.status_code
