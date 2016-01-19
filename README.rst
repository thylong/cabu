Cabu
====

.. image:: https://readthedocs.org/projects/cabu/badge/?version=latest
    :target: http://cabu.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

Cabu is a simple microservice framework to remotely crawl websites.
It's built on Flask and Selenium, contains a virtual display wrapper and few methods.

`Full documentation here`_

Usage
=====

.. code-block:: python

    @app.route('/gizmodo_last_articles_links')
    def gizmodo_last_articles():
        app.webdriver.get('http://www.gizmodo.com')
        articles_links = [i.get_attribute('href') for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')]

        return jsonify({'articles': articles_links})


Installing
==========


.. code-block:: console

    $ pip install cabu

Features
========

- Selenium configuration out of the box
- Flask wrapping
- Crawling methods included
- AWS S3 Export
- FTP / FTPS
- Cookies persistence
- Link extractor
- Proxy configuration
- Headless optional for local debug
- Docker pre-configured distributed environment
- Database handler
- Compatible with most Flask extensions (Flask-Admin, Flask-Mail, Flask-OAuth, ...)
- 12 Factors compliance

(Likely to come soon)

- CouchDB support
- Couchbase support
- Mobile drivers
- SFTP
- HtmlUnit web driver
- Remote webdriver wrapper
- Parallelization
- Neural Network plugins


Testing
=======

All tests were written using Docker services instead of Mocks.
Alternative mocks will be added soon ;)

.. code-block:: console

    $ pip install -r requirements-dev.txt
    $ py.test cabu/tests

Contributing
============

Please see the `Contribute page`_.

Copyright
=========

Cabu is an open source project by `Théotime Lévèque`_.


.. _`Full documentation here`: https://cabu.readthedocs.org/
.. _`Contribute page`: https://cabu.readthedocs.org/contribute
.. _`Théotime Lévèque`: https://github.com/thylong
