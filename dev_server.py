# -*- coding: utf-8 -*-

import os
from cabu import Cabu
from flask import jsonify

os.environ['DRIVER_NAME'] = 'PhantomJS'
# os.environ['DRIVER_NAME'] = 'Firefox'
# os.environ['DRIVER_BINARY_PATH'] = 'iceweasel'
app = Cabu(__name__)


@app.route('/gizmodo_last_articles_links')
def gizmodo_last_articles():
    app.webdriver.get('http://www.gizmodo.com')
    articles_links = [
        i.get_attribute('href')
        for i in app.webdriver.find_elements_by_css_selector('h1.headline>a')
    ]

    return jsonify({'message': 'Last articles', 'articles': articles_links})


@app.route('/test_headers')
def test_headers():
    app.webdriver.get('http://requestb.in/11vj4ii1')

    return jsonify({'message': 'Test header', 'status': 'ok'})

app.run(host='0.0.0.0', port=8080, debug=True)
