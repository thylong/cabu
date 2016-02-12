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
