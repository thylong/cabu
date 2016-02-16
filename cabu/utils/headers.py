# -*- coding: utf-8 -*-

from cabu.exceptions import HeaderException


class Headers(object):
    """Abstract layer on top of webdrivers.

    Args:
        config (dict): The config dict.
    """
    def __init__(self, config):
        self.driver_name = config['DRIVER_NAME']
        self.headers = config['HEADERS']

    def set_headers(self, profile):
        """Generate profile for headers config.

        Args:
            profile (object): The profile object of the webdriver.

        Returns:
            profile (object): The object to pass as argument to the webdriver.
        """
        self.profile = profile

        for header_key, header_value in self.headers.items():
            self.profile = self.set_header(header_key, header_value)
        return self.profile

    def set_header(self, header_key, header_value):
        """Set the value of the defined header key.

        Args:
            key (str): The name of the header key to set.
            value (str): The value associated to the header key to set.

        Returns:
            profile (object): The object to pass as argument to the webdriver.
        """
        if self.driver_name == 'Firefox':
            # See more Options here :
            # https://github.com/SeleniumHQ/selenium/blob/master/javascript/firefox-driver/webdriver.json
            header_key = header_key.lower().replace('-', '')
            self.profile.set_preference('general.%s.override' % header_key, header_value)
        elif self.driver_name == 'PhantomJS':
            # See more Options here :
            # https://github.com/ariya/phantomjs/wiki/API-Reference-WebPage
            self.profile["phantomjs.page.customHeaders.%s" % header_key] = (
                header_value
            )
        else:
            raise HeaderException('Webdriver not supported for now.')

        return self.profile
