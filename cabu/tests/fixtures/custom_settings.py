# -*- coding: utf-8 -*-

DEBUG = True
CABU_TEST = None

CABU_SETTINGS = 'cabu.default_settings'

DRIVER_NAME = 'PhantomJS'
DRIVER_BINARY_PATH = None
# DRIVER_BINARY_PATH = '/Users/t.leveque/Applications/Firefox.app/Contents/MacOS/firefox'
DRIVER_WINDOWS_WIDTH = 800
DRIVER_WINDOWS_HEIGHT = 600
DRIVER_PAGE_TIMEOUT = 10  # In seconds.

FTP_HOST = None
FTP_LOGIN = None
FTP_PASSWORD = None

HEADLESS = True  # Run the Browser in Xvfd
HEADERS = {
    'User-Agent':
        'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_3) Apple'
        'WebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
}

IO_CONCURRENCY = False  # If True, Python version should be superior or equal to py34

DATABASE_URI = 'mongodb://localhost/test'
