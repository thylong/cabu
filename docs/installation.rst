.. _installation:

Installation
============

You can either install Cabu localy or remotely.
The only thing you've to ensure at least, is to install external dependencies
listed below.

Dependencies
------------
Cabu dependencies can be separated into 3 categories. If you don't care about
selenium.webdriver features, install only strict requirements otherwise at least
one webdriver is needed.

**Required:**

Cabu contains a few dependencies listed in his requirements.txt which are
installed by default.

.. code-block:: console

    $ pip install cabu

With this basic setup, you have a working instance of Cabu.

**Recommended:**

To have a taste of Cabu's features, install the virtual display Xvfb_

.. code-block:: bash

    # for Debian based Linux distributions
    apt-get install xvfb


Choose and install a webdriver between :

- phantomJS_ *(light and fast, recommended to start)*
- Firefox_
- Chrome_ (require a little bit of Selenium knowledge)

.. code-block:: bash

    # for Debian based Linux distributions
    apt-get install your_selected_driver
    # for Mac OS X
    brew install your_selected_driver


Configuration
-------------

Cabu can be configured using a settings.py file or environment variables or both.
You can find all the possible parameters in the default_settings.py in cabu/
folder.

Be careful, environments variables are prioritized over configuration files.

For example to use Firefox :

.. code-block:: bash

    # Using environment variables
    export $DRIVER_NAME=Firefox
    # Using settings.py
    DRIVER_NAME = 'Firefox'



.. _Xvfb: http://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml
.. _phantomJS: http://phantomjs.org/
.. _Firefox: https://www.mozilla.org/en-US/
.. _Chrome: https://www.google.com/chrome/browser/desktop/index.html
