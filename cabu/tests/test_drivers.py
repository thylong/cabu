# -*- coding: utf-8 -*-

import os
from cabu.drivers import load_driver, unload_driver
from cabu.exceptions import DriverException
from cabu.tests.test_base import TestBase

from mock import patch, Mock, MagicMock


class TestDrivers(TestBase):
    def test_load_no_driver(self):
        self.config['DRIVER_NAME'] = None
        load_driver(self.config)

    def test_load_unrecognized_driver(self):
        self.config['DRIVER_NAME'] = 'Netscape'
        with self.assertRaises(DriverException):
            load_driver(self.config)

    @patch('cabu.drivers.load_phantomjs', return_value=MagicMock())
    def test_load_driver(self, mock_driver):
        driver = load_driver(self.config)
        mock_driver.assert_called_once_with(self.config)
        unload_driver(driver)

    @patch('cabu.drivers.load_phantomjs', return_value=MagicMock())
    def test_unload_driver_fail(self, mock_driver):
        driver = load_driver(self.config)
        mock_driver.assert_called_once_with(self.config)
        driver.close = Mock()
        driver.close.side_effect = Exception('Boom !')
        unload_driver(driver)

    @patch('cabu.drivers.webdriver.Firefox', return_value=MagicMock())
    def test_load_firefox(self, mock_driver):
        self.config['DRIVER_NAME'] = 'Firefox'
        driver = load_driver(self.config)
        driver.close()

    @patch('cabu.drivers.webdriver.Firefox', return_value=MagicMock())
    def test_load_firefox_with_binary(self, mock_driver):
        self.config['DRIVER_NAME'] = 'Firefox'
        self.config['DRIVER_BINARY_PATH'] = 'firefox'
        driver = load_driver(self.config)
        driver.close()

    @patch('cabu.drivers.webdriver.Firefox', return_value=MagicMock())
    def test_load_firefox_with_headers(self, mock_driver):
        self.config['DRIVER_NAME'] = 'Firefox'
        self.config['HEADERS'] = {
            'User-Agent':
                'Mozilla/7.0 (Macintosh; Intel Mac OS X 10_11_3) Apple'
                'WebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.10'
                '3 Safari/537.36'
        }
        driver = load_driver(self.config)
        driver.close()

    @patch('cabu.drivers.webdriver.Chrome', return_value=MagicMock())
    def test_load_chrome(self, mock_driver):
        self.config['DRIVER_NAME'] = 'Chrome'
        driver = load_driver(self.config)
        mock_driver.assert_called_once_with()
        driver.close()

    @patch('cabu.drivers.webdriver.PhantomJS', return_value=MagicMock())
    @patch('cabu.drivers.DesiredCapabilities', return_value='mock_dcap')
    def test_load_phantomjs(self, mock_dcap, mock_driver):
        self.config['DRIVER_NAME'] = 'PhantomJS'
        driver = load_driver(self.config)
        mock_driver.assert_called_once_with(
            desired_capabilities={},
            service_args=[
                '--ignore-ssl-errors=true',
                '--ssl-protocol=any',
                '--web-security=false'
            ],
            service_log_path='/dev/null'
        )
        driver.close()

    @patch('cabu.drivers.webdriver.PhantomJS', return_value=MagicMock())
    @patch('cabu.drivers.DesiredCapabilities', return_value='mock_dcap')
    def test_load_phantomjs_with_headers(self, mock_dcap, mock_driver):
        self.config['DRIVER_NAME'] = 'PhantomJS'
        self.config['HEADERS'] = {
            'User-Agent':
                'Mozilla/7.0 (Macintosh; Intel Mac OS X 10_11_3) Apple'
                'WebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.10'
                '3 Safari/537.36'
        }
        driver = load_driver(self.config)
        driver.close()

    @patch('cabu.drivers.webdriver.Firefox', return_value=MagicMock())
    def test_load_with_firefox_http_proxy(self, mock_driver):
        self.config['DRIVER_NAME'] = 'Firefox'
        os.environ['HTTP_PROXY'] = 'http://127.0.0.1:80'
        driver = load_driver(self.config)
        driver.close()

    @patch('cabu.drivers.webdriver.Firefox', return_value=MagicMock())
    def test_load_with_firefox_https_proxy(self, mock_driver):
        self.config['DRIVER_NAME'] = 'Firefox'
        os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:80'
        driver = load_driver(self.config)
        driver.close()

    @patch('cabu.drivers.webdriver.PhantomJS', return_value=MagicMock())
    @patch('cabu.drivers.DesiredCapabilities', return_value='mock_dcap')
    def test_load_with_phantomjs_http_proxy(self, mock_dcap, mock_driver):
        os.environ['HTTP_PROXY'] = 'http://127.0.0.1:80'
        driver = load_driver(self.config)
        mock_driver.assert_called_once_with(
            desired_capabilities={},
            service_args=[
                '--ignore-ssl-errors=true',
                '--ssl-protocol=any',
                '--web-security=false',
                '--proxy=127.0.0.1:80',
                '--proxy-type=http'
            ],
            service_log_path='/dev/null'
        )
        driver.close()

    @patch('cabu.drivers.webdriver.PhantomJS', return_value=MagicMock())
    @patch('cabu.drivers.DesiredCapabilities', return_value='mock_dcap')
    def test_load_with_phantomjs_https_proxy(self, mock_dcap, mock_driver):
        os.environ['HTTP_PROXY'] = 'http://127.0.0.1:80'
        driver = load_driver(self.config)
        mock_driver.assert_called_once_with(
            desired_capabilities={},
            service_args=[
                '--ignore-ssl-errors=true',
                '--ssl-protocol=any',
                '--web-security=false',
                '--proxy=127.0.0.1:80',
                '--proxy-type=http'
            ],
            service_log_path='/dev/null'
        )
        driver.close()
