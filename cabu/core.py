# -*- coding: utf-8 -*-

"""
    Cabu.auth
    ~~~~~~~~~~~~~~

    Cabu is a simple microservice framework to crawl websites.

    :copyright: (c) 2015 by Théotime Leveque.
    :license: BSD, see LICENSE_FILE for more details.
"""

import sys
import os
from ftpretty import ftpretty
from six import string_types
from flask import Flask
from cabu.drivers import load_driver, load_vdisplay
from cabu.drivers import unload_driver, unload_vdisplay
from cabu.exceptions import ConfigurationException
from cabu.utils.bucket import Bucket
from cabu.utils.cookies import CookieStorage


class Cabu(Flask):
    def __init__(self, import_name=__package__, db=None, *args, **kwargs):
        """Cabu main class, acts as a WSGI interface.

        It overrides Flask to include the config, the Selenium WebDriver,
        the Database, eventually an S3 bucket and a FTP.

        Args:
            import_name (str): Same as for Flask initialization.
            db (Optional[object]): The database driver class. Defaults to None.

        Returns:
            object: A Flask instance plus Cabu specific attributes.
        """
        super(Cabu, self).__init__(import_name, **kwargs)
        settings_path = os.environ.get('CABU_SETTINGS', 'cabu.default_settings')
        self.load_config(settings_path)

        if db:
            if 'DATABASE_URI' not in self.config:
                if db.__name__ == 'PyMongo':
                    default_uri = 'mongodb://localhost/%s' % self.name
                else:
                    raise ConfigurationException(
                        'Unknown database missing DATABASE_URI setting.'
                    )

                self.config['DATABASE_URI'] = os.environ.get(
                    'DATABASE_URI', default_uri
                )
            mongo = db(self, config_prefix='DATABASE')
            with self.app_context():
                self.db = mongo.db
                self.cookies = CookieStorage(self.db)

        if self.config.get('S3_BUCKET'):
            self.bucket = Bucket(
                self.config['S3_BUCKET'],
                self.config['S3_ACCESS_KEY'],
                self.config['S3_SECRET_KEY']
            )

        if self.config.get('FTP_HOST'):
            self.ftp = ftpretty(
                self.config['FTP_HOST'],
                self.config['FTP_LOGIN'],
                self.config['FTP_PASSWORD']
            )

        self.vdisplay = load_vdisplay(self.config)
        self.webdriver = load_driver(self.config, self.vdisplay)

    def __del__(self):
        if hasattr(self, 'ftp'):
            self.ftp.close()
        if hasattr(self, 'webdriver'):
            unload_driver(self.webdriver)
        if hasattr(self, 'vdisplay'):
            unload_vdisplay(self.vdisplay)

    def __exit__(self, *args, **kwargs):  # pragma: no cover
        if hasattr(self, 'ftp'):
            self.ftp.close()
        if hasattr(self, 'webdriver'):
            unload_driver(self.webdriver)
        if hasattr(self, 'vdisplay'):
            unload_vdisplay(self.vdisplay)
        super(Cabu, self).__exit__(*args, **kwargs)

    def __getattr__(self, name):
        if name in ['webdriver', 'db', 'ftp', 'bucket']:
            raise AttributeError('Cabu was initialized without a %s.' % name)
        else:
            raise AttributeError

    def load_config(self, settings='cabu.default_settings'):
        """Get the given settings module to create a config dict in the class.

        All variables defined in upper case in the settings module are imported
        in the directory and overrided by the corresponding environment
        variables.

        Args:
            settings (Optional[str]): A module path where stands the settings.
        """
        if isinstance(settings, string_types):
            import_name = str(settings)
            try:
                __import__(import_name)
            except ImportError as e:
                if '.' not in import_name:
                    raise ImportError(e)
            else:
                for key in dir(sys.modules[import_name]):
                    if key.isupper():
                        self.config[key] = getattr(
                            sys.modules[import_name], key
                        )

        # settings.py are overriden by Env vars.
        for key in self.config.keys():
            if key.isupper() and key in os.environ:
                if os.environ[key] == 'True':
                    self.config[key] = True
                elif os.environ[key] == 'False':
                    self.config[key] = False
                else:
                    self.config[key] = os.environ[key]
