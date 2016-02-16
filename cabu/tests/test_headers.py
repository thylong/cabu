# -*- coding: utf-8 -*-

from cabu.tests.test_base import TestBase
from cabu.utils.headers import Headers
from mock import patch

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


class TestHeaders(TestBase):
    def setUp(self):
        super(TestHeaders, self).setUp()
        self.patcher_phantomjs = patch('cabu.drivers.load_phantomjs', spec=True)
        self.patcher_phantomjs.start()

        self.config = self.app.config
        self.config['HEADERS'] = {
            'User-Agent':
                'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_3) Apple'
                'WebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
        }

    def tearDown(self):
        super(TestHeaders, self).setUp()
        self.patcher_phantomjs.stop()

    def test_firefox_headers_loading(self):
        self.app.config['DRIVER_NAME'] = 'Firefox'
        profile = webdriver.FirefoxProfile()
        headers = Headers(self.app.config)
        profile = headers.set_headers(profile)
        self.assertEquals(
            profile.__dict__['default_preferences']['general.useragent.override'],
            'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
        )

    def test_phantomjs_headers_loading(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        headers = Headers(self.config).set_headers(dcap)
        self.assertEquals(
            headers['phantomjs.page.customHeaders.User-Agent'],
            'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
        )

    def test_chrome_headers_loading(self):
        self.app.config['DRIVER_NAME'] = 'Chrome'
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        with self.assertRaises(Exception):
            Headers(self.config).set_headers(dcap)
