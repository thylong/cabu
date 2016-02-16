# -*- coding: utf-8 -*-

"""
    Cabu.exceptions
    ~~~~~~~~~~~~~~

    Cabu is a simple microservice framework to crawl websites.

    :copyright: (c) 2015 by Théotime Leveque.
    :license: BSD, see LICENSE_FILE for more details.
"""


class SkipingException(Exception):
    pass


class LinkExtractorException(Exception):
    pass


class ConfigurationException(Exception):
    pass


class CookieStorageException(Exception):
    pass


class HeaderException(Exception):
    pass


class DriverException(Exception):
    pass
