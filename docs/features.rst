.. _features:

Features
========

Selenium webdrivers wrapper
---------------------------

The main force of Cabu is his ability to abstract Flask and Selenium setup to
give you an out of the box crawling or remote testing system.

Global Objects
--------------

Cabu adds a little of magic to your app. How ? By adding few attributes and
methods that are globally accessible during the runtime of your app.

========== ============================================
Properties Description
========== ============================================
webdriver  The selenium webdriver of the configuration
vdisplay   An instance of xvfb-virtualwrapper
db         An instance of your selected DB driver
bucket     A S3 driver (requests-aws)
ftp        A ftpretty instance
cookies    A cookies handler
========== ============================================

Database storage
----------------

Because of his modular nature, Cabu can be extended at anytime.
You can use no database or Mongo (soon CouchDB and CouchBase), depending on your
needs.

First, you need to install and configure a Database extension.

.. code-block:: python

    from cabu import Cabu
    from flask.ext.pymongo import PyMongo

    app = Cabu(__name__, db=PyMongo)

Then, you can use Database python driver native methods.

.. code-block:: python

    def get_beers():
        beers_page = app.webdriver.get('http://beers.com')
        titles = beers_page.findAll('title')
        app.db.insert(titles)

        return jsonify({
            'message': 'Last articles',
            'articles': articles_links,
        })

Link extractor
--------------

The link extractor methods allow you to extract links from an HTTP Response
Object and retrieve them as a list.

You can filter this list using optional arguments defined in the API.

Example :

.. code-block:: python

    @app.route('/home_wikipedia')
    def get_wiki_links():
        requests.get('http://en.wikipedia.org')
        # list only anchors
        links = extract_links(re='^#')
        return jsonify({'links': links})

Cookies persistence
-------------------

If you've set up a database, you can persist cookies in it. This way, cookies
can be regenerated only when necessary (it's particularly useful to manage
authentification).

.. code-block:: python

    app.cookies.set('wiki_cookie', 'en.wikipedia.org')
    app.cookies.get('wiki_cookie')

S3/FTP Export
-------------

Data scrapped can be exported to an Amazon S3 bucket if the key is provided in
the configuration.

.. code-block:: python

    S3_BUCKET = '2348902r09f2j4039bbbq9bpr2fff2'  # settings.py
    app.bucket.put({
        'title': title,
        'description': 'A little garden from %s' % author,
        'content': page_content
    })

Proxy
-----

It's possible to use a specific proxy or a list of proxy to make random origin
calls. The only thing to do is to specify the proxy(ies) in the configuration as
a list.

Cabu will use the following by default.

.. code-block:: python

    HTTP_PROXY = ['127.0.0.1']
    # or with HTTPS
    HTTPS_PROXY = ['127.0.0.1']
