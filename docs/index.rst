.. Cabu documentation master file, created by
   sphinx-quickstart on Fri Jan 15 00:48:40 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Cabu's documentation!
================================

Cabu is a simple framework to create crawling microservices.

    **Jean Cabut** (1938 – 2015), known by the pen-name **Cabu**, was a French
    caricaturist. He died in the January 2015 shooting attack at the Charlie
    Hebdo offices. Today he still stands as a source of inspiration for many
    people in France.

Introduction
------------

Following the philosophy of Python, Cabu wants to be easy to use and simple to
understand.
It's suitable for deployment on modern cloud platforms and constructed as a
modular package so you can start with the default setup or customize pretty much
everything. It's also based on Flask_ and Selenium_ and works on Python
interpreter versions prior to 2.6 (including PyPy).

No more talk :

No headaches
------------

This is a simple example of how to define an endpoint to get the list of last Gizmodo articles :

.. code-block:: python

    from cabu import Cabu

    app = Cabu(__name__)

    @app.route('/gizmodo_last_articles_links')
    def gizmodo_last_articles():
        app.webdriver.get('http://www.gizmodo.com')
        articles_links = [
            i.get_attribute('href')
            for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')
        ]

        return jsonify({'message': 'Last articles', 'articles': articles_links})

    app.run()


Contents:
---------

.. toctree::
   :maxdepth: 2

   installation
   philosophy
   quickstart
   features
   examples
   support
   contribute
   licensing
   changelog
   api

.. _Flask: http://flask.pocoo.org/
.. _Selenium: http://docs.seleniumhq.org/
