.. _examples:

Examples
========

Few examples of what you can do with Cabu.

Simple example
--------------

.. code-block:: python

    @app.route('/gizmodo_last_articles_links')
    def gizmodo_last_articles():
        app.webdriver.get('http://www.gizmodo.com')
        articles_links = [i.get_attribute('href') for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')]

        return jsonify({
            'message': 'Last articles',
            'articles': articles_links,
        })


Persistence
-----------

You can persist what you crawl to a database.

.. code-block:: python

    @app.route('/store_gizmodo_last_articles_links')
    def store_gizmodo_last_articles():
        app.webdriver.get('http://www.gizmodo.com')
        articles_links = [i.get_attribute('href') for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')]
        app.db.links.insertMany(articles_links)

        return jsonify({
            'message': 'Last articles from Gizmodo',
            'nb_articles_inserted': len(articles_links),
        })


Export links of a page to S3
-------------------------------------------

But also to a S3 bucket :)

.. code-block:: python

    @app.route('/export_gizmodo_last_articles_links')
    def export_gizmodo_last_articles():
        app.webdriver.get('http://www.gizmodo.com')
        articles_links = [i.get_attribute('href') for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')]
        app.bucket.put('my_links.txt', articles_links)

        return jsonify({
            'message': 'Last articles from Gizmodo',
            'nb_articles_inserted': len(articles_links),
        })


More complex scenario
---------------------

.. code-block:: python

    @app.route('/cheapest_flight')
    def cheapest_flight():
        app.webdriver.get('https://www.expedia.com')
        homepage = app.webdriver.find_element_by_tag_name('html')
        tab_flight = app.webdriver.find_element_by_id('tab-flight-tab')
        tab_flight.click()

        # Selecting from elements
        origin_input = app.webdriver.find_element_by_id('flight-origin')
        destination_input = app.webdriver.find_element_by_id('flight-destination')
        departure_date_input = app.webdriver.find_element_by_id('flight-departing')
        return_date_input = app.webdriver.find_element_by_id('flight-returning')
        search_button = app.webdriver.find_element_by_id('search-button')

        # Filling infos + validation
        origin_input.send_keys('New York, NY (NYC-All Airports)')
        destination_input.send_keys('Paris, France (PAR-All Airports)')
        return_date_input.clear()

        departure_date_input.send_keys('06/01/2016')
        return_date_input.click()
        return_date_input.clear()
        return_date_input.send_keys('09/15/2016')
        search_button.click()

        WebDriverWait(app.webdriver, 60).until(staleness_of(homepage))

        # Scrap the cheapest
        flight = {}
        try:
            flight['departure_time'] = app.webdriver.find_element_by_css_selector('span.departure-time').text + 'm'
            flight['arrival_time'] = app.webdriver.find_element_by_css_selector('#flightModule1 span.arrival-time').text + 'm'
            flight['airline'] = app.webdriver.find_element_by_css_selector('#flightModule1 div.truncate').text
            flight['price'] = app.webdriver.find_element_by_css_selector('#flightModule1 .dollars').text
        except NoSuchElementException:
            message = 'No results :('
        else:
            message = 'Results retrieved !'

        return jsonify({
            'message': message,
            'flight': flight,
            'search_url': app.webdriver.current_url
        })
