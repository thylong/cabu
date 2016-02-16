# -*- coding: utf-8 -*-

import os
import re
from selenium import webdriver
from xvfbwrapper import Xvfb
from cabu.exceptions import DriverException
from cabu.utils.headers import Headers
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

try:
    from urllib.parse import urlsplit
except ImportError:  # pragma: no cover
    from urlparse import urlsplit  # flake8: noqa


def load_vdisplay(config):
    """Initialize a vdisplay (Xvfb subprocess instance).

    Args:
        config (dict): The configuration loaded previously in Cabu.

    Returns:
        vdisplay: An instance of Xvfb wrapper.
    """

    vdisplay = None

    if config['HEADLESS']:
        vdisplay = Xvfb(
            width=config['DRIVER_WINDOWS_WIDTH'],
            height=config['DRIVER_WINDOWS_HEIGHT']
        )
        vdisplay.start()

    return vdisplay


def unload_vdisplay(vdisplay):
    """Shutdown given Xvfb instance.

    Args:
        vdisplay (XvfbWrapper): The running virtual X server.
    """
    vdisplay.stop()


def load_driver(config, vdisplay=None):
    """Initialize a weddriver selected in config with given config.

    Args:
        config (dict): The configuration loaded previously in Cabu.

    Returns:
        webdriver (selenium.webdriver): An instance of selenium webdriver or None.
    """

    if config['DRIVER_NAME'] == 'Firefox':
        driver = load_firefox(config)
    elif config['DRIVER_NAME'] == 'Chrome':
        driver = load_chrome(config)
    elif config['DRIVER_NAME'] == 'PhantomJS':
        driver = load_phantomjs(config)
    elif not config.get('DRIVER_NAME'):
        return None
    else:
        raise DriverException(vdisplay, 'Driver unrecognized.')

    driver.set_page_load_timeout(config['DRIVER_PAGE_TIMEOUT'])
    driver.set_window_size(config['DRIVER_WINDOWS_WIDTH'], config['DRIVER_WINDOWS_HEIGHT'])

    return driver


def unload_driver(driver):
    """Shutdown given webdriver instance.

    Args:
        driver (selenium.webdriver): The running webdriver.
    """
    driver.quit()


def load_firefox(config):
    """Start Firefox webdriver with the given configuration.

    Args:
        config (dict): The configuration loaded previously in Cabu.

    Returns:
        webdriver (selenium.webdriver): An instance of Firefox webdriver.

    """
    binary = None
    profile = webdriver.FirefoxProfile()

    if os.environ.get('HTTPS_PROXY') or os.environ.get('HTTP_PROXY'):
        proxy_address = os.environ.get('HTTPS_PROXY', os.environ.get('HTTP_PROXY'))
        proxy_port = re.search('\:([0-9]+)$', proxy_address).group(1)

        profile.set_preference('network.proxy.type', 1)
        profile.set_preference(
            'network.proxy.http',
            proxy_address
        )
        profile.set_preference('network.proxy.http_port', proxy_port)
        profile.update_preferences()

    if 'HEADERS' in config and config['HEADERS']:
        profile = Headers(config).set_headers(profile)

    if config['DRIVER_BINARY_PATH']:
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary(config['DRIVER_BINARY_PATH'])

    return webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)


def load_chrome(config):
    """Start Chrome webdriver with the given configuration.

    Args:
        config (dict): The configuration loaded previously in Cabu.

    Returns:
        webdriver (selenium.webdriver): An instance of Chrome webdriver.

    """
    return webdriver.Chrome()


def load_phantomjs(config):
    """Start PhantomJS webdriver with the given configuration.

    Args:
        config (dict): The configuration loaded previously in Cabu.

    Returns:
        webdriver (selenium.webdriver): An instance of phantomJS webdriver.

    """
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    service_args = [
        '--ignore-ssl-errors=true',
        '--ssl-protocol=any',
        '--web-security=false'
    ]

    if os.environ.get('HTTPS_PROXY') or os.environ.get('HTTP_PROXY'):
        proxy_address = os.environ.get('HTTPS_PROXY', os.environ.get('HTTP_PROXY'))
        proxy_ip = re.search('http\:\/\/(.*)$', proxy_address).group(1)
        service_args.append('--proxy=%s' % proxy_ip)
        service_args.append('--proxy-type=http')

    if 'HEADERS' in config and config['HEADERS']:
        dcap = Headers(config).set_headers(dcap)

    return webdriver.PhantomJS(
        desired_capabilities=dcap,
        service_args=service_args,
        service_log_path=os.path.devnull
    )
