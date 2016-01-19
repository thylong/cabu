.. _philosophy:

Philosophy
==========

Cabu was created to be a part of the new kind of applications that make more
sense remotely than locally. Following as close as possible the `12 Factors`_ rules
makes it more reliable, flexible and trustable being in the cloud.

Because of his nature, and because Cabu was designed using Docker, It can make
sense to use Docker tools and ecosystem to build, ship and run your
application.

Modular
-------

With the minimal configuration, you can crawl a website using requests or
aiohttp depending on your need and your Python version. With a webdriver set up,
you can crawl with a real browser and you can do more with a little bit of
configuration. In few words, this project is modular. You start with almost
nothing and it's up to you to integrate modules or external services.

Some use cases :

- Functionaly test a website
- Crawl periodically some data
- Act as a data mining bot
- Crawling an entire website (using several instances)


If your need is to crawl only from a local crawler, there is already a lot of
tools to do that, Scrapy_ is one of the most famous and convenient to use. Cabu
aims to make you able to create a crawler in the cloud in very few steps and
work.

Cabu is social
--------------

This kind of tool makes more sense when integrated into a distributed
system. Because it's a Flask extension, it's compatible with a lot of Flask
plugins. Also, because you'll communicate with your crawlers only using HTTP, it's
easy to integrate it with an asynchronous tasks manager like ØMQ_ or Hooky_,
to set a NGINX proxy in front of it, etc.
Even the database is not included. This way, it's again up to you to make your
application communicate with a Mongo in SaaS or only export to a FTP or an S3 bucket.

... And has a best friend
-------------------------

Using Docker and Docker-compose tool will make the development kick-off a matter
of few seconds. You can find the Dockerfile configuration at the root of the
project or here_.

I hope you will enjoy this project, cheers !

.. _Scrapy: http://scrapy.org/
.. _ØMQ: http://zeromq.org/
.. _Hooky: https://github.com/sebest/hooky
.. _here: https://hub.docker.com/r/thylong/cabu/
.. _`12 Factors`: http://12factor.net/
