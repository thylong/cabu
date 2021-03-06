# -*- coding: utf-8 -*-

from cabu.core import Cabu
from cabu.tests.test_base import TestBase
from flask.ext.pymongo import PyMongo

from mock import patch, MagicMock


class TestCookiesStorage(TestBase):
    @patch('cabu.drivers.load_phantomjs', return_value=MagicMock())
    def setUp(self, mock_driver):
        self.app = Cabu(__name__, db=PyMongo)
        self.cookies = self.app.cookies

    def test_crud(self):
        r = self.cookies.set('test', 'test')
        self.assertIsInstance(r, dict)
        self.assertEqual(r['ok'], 1)

        r = self.cookies.get('test')
        self.assertIsInstance(r, dict)
        self.assertEqual(r['test'], 'test')

        r = self.cookies.delete('test')
        self.assertEqual(r['ok'], 1)

    def test_clean(self):
        self.cookies.set('test1', 'test')
        self.cookies.set('test2', 'test')
        r = self.cookies.clean()
        self.assertEqual(r['ok'], 1)
