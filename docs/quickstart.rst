.. _quickstart:

Quickstart
==========

One you installed Cabu, as any application extending Flask, you can create
routes and execute whatever you want inside.

Initialize Selenium with a WebDriver
------------------------------------

You can use Cabu without Selenium, but it's not really the most interesting way
to crawl. To have a look at the potential of Cabu, you should install Firefox or
PhantomJS and Xvfb.

If you're familiar with Docker, I suggest you to check the Dockerfile and
docker-compose files. If not :

.. code-block:: console

    $ apt-get install xvfb

    $ apt-get install phantomjs


and then try to create a app.py file :

.. code-block:: python

    from cabu import Cabu
    app = Cabu(__name__)

    @app.route('/gizmodo_last_articles_links')
    def gizmodo_last_articles():
        app.webdriver.get('http://www.gizmodo.com')
        articles_links = [i.get_attribute('href') for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')]

        return jsonify({'message': 'Last articles', 'articles': articles_links})
    app.run()

Then you can run the WSGI application :

.. code-block:: console

    $ python app.py

And finally query it (using either httpie_ or curl_ or you're favorite http
tool) :

.. code-block:: console

    $ http 'localhost/gizmodo_last_articles_links'

Wait... Nothing happened ? That's normal :

Debug locally
-------------

Cabu uses headless webdriver by default but during development it's always nice
to see what's going on without having to take screenshot again and again...

If you set the HEADLESS settings parameter (or environment variable) to True
the webdriver is going to be displayed using current display.

.. code-block:: console

    $ export $HEADLESS=true

.. admonition:: Please note

    Depending on the unix OS you're using to run Cabu, the path to webdriver binary can vary.
    If you're not using the Docker image, I suggest you to set the $DRIVER_BINARY_PATH environment variable.

    For OS X :

    .. code-block:: console

        $ export $DRIVER_BINARY_PATH=/Users/<your_user>/Applications/Firefox.app/Contents/MacOS/firefox

Basic features
--------------

Check the :doc:`features` page.

Cabu through examples
---------------------

Check the :doc:`examples` page.

Cabu in production
------------------

Don't waste your time, extend the official Docker build repository_.

.. _repository: https://hub.docker.com/r/thylong/cabu/
.. _httpie: https://github.com/jkbrzt/httpie
.. _curl: http://curl.haxx.se/
