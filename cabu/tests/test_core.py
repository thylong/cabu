# -*- coding: utf-8 -*-

import os
from flask.ext.pymongo import PyMongo
from flask_pymongo.wrappers import Database
from cabu.tests.test_base import TestBase
from cabu.exceptions import ConfigurationException
from cabu import Cabu

from mock import patch


class TestCore(TestBase):
    def setUp(self):
        self.patcher_load_phantomjs = patch('cabu.drivers.load_phantomjs', spec=True)
        self.patcher_load_phantomjs.start()
        if 'CABU_SETTINGS' in os.environ:
            del os.environ['CABU_SETTINGS']

    def tearDown(self):
        self.patcher_load_phantomjs.stop()

    def test_cabu_default(self):
        cabu = Cabu(__name__)
        self.assertIsInstance(cabu, Cabu)
        self.assertEquals(cabu.config['DRIVER_NAME'], 'PhantomJS')
        self.assertEquals(cabu.config['DRIVER_WINDOWS_WIDTH'], 1024)
        self.assertEquals(cabu.config['DRIVER_WINDOWS_HEIGHT'], 768)
        self.assertEquals(cabu.config['DRIVER_PAGE_TIMEOUT'], 30)
        self.assertEquals(cabu.config['IO_CONCURRENCY'], False)
        self.assertEquals(cabu.config['HEADLESS'], True)
        del cabu

    def test_cabu_test_boolean_var_env(self):
        os.environ['CABU_TEST'] = 'True'
        cabu = Cabu(__name__)
        self.assertEquals(cabu.config['CABU_TEST'], True)
        del cabu

        os.environ['CABU_TEST'] = 'False'
        cabu = Cabu(__name__)
        self.assertEquals(cabu.config['CABU_TEST'], False)
        del cabu

    def test_cabu_custom(self):
        os.environ['CABU_SETTINGS'] = 'cabu.tests.fixtures.custom_settings'
        cabu = Cabu(__name__)
        self.assertIsInstance(cabu, Cabu)
        self.assertEquals(cabu.config['DRIVER_NAME'], 'PhantomJS')
        self.assertEquals(cabu.config['DRIVER_WINDOWS_WIDTH'], 800)
        self.assertEquals(cabu.config['DRIVER_WINDOWS_HEIGHT'], 600)
        self.assertEquals(cabu.config['DRIVER_PAGE_TIMEOUT'], 10)
        self.assertEquals(cabu.config['IO_CONCURRENCY'], False)
        self.assertEquals(cabu.config['HEADLESS'], True)
        del cabu

    def test_cabu_load_with_db(self):
        cabu = Cabu(__name__, db=PyMongo)
        self.assertIsInstance(cabu.db, Database)
        del cabu

    def test_cabu_load_with_unrecognized_db(self):
        with self.assertRaises(ConfigurationException):
            cabu = Cabu(__name__, db=os)
            del cabu

    def test_cabu_wrong_settings_path(self):
        os.environ['CABU_SETTINGS'] = 'cabutestsfixturescustom_settings'
        with self.assertRaises(ImportError):
            cabu = Cabu(__name__)
            del cabu
