# -*- coding: utf-8 -*-

from cabu.tests.test_base import TestBase
from cabu.utils.link_extractor import extract_links, filter_links
from cabu.exceptions import LinkExtractorException


class TestLinkExtractor(TestBase):
    def test_extract_links(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        links = extract_links(response)
        self.assertEquals(links, ['http://tomato.org/test', 'http://tomato.com/test'])

    def test_extract_links_common_white_and_black_lists(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        with self.assertRaises(LinkExtractorException):
            extract_links(response, whitelist_domains=['test'], blacklist_domains=['test'])

    def test_extract_unique_links(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.org/test</a>'
        links = extract_links(response, unique=True)
        self.assertEquals(links, ['http://tomato.org/test'])

    def test_extract_links_with_regex(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        links = extract_links(response, regex='tomato\.org')
        self.assertEquals(links, ['http://tomato.org/test'])

    def test_extract_links_with_whitelist_domains(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        links = extract_links(response, whitelist_domains=['tomato.org'])
        self.assertEquals(links, ['http://tomato.org/test'])

    def test_extract_links_with_blacklist_domains(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        links = extract_links(response, blacklist_domains=['tomato.org'])
        self.assertEquals(links, ['http://tomato.com/test'])

    def test_extract_links_with_whitelist_extensions(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        links = extract_links(response, whitelist_extensions=['.org'])
        self.assertEquals(links, ['http://tomato.org/test'])

    def test_extract_links_with_blacklist_extensions(self):
        response = '<a>http://tomato.org/test</a><b>http://tomato.org/test</b><a>http://tomato.com/test</a>'
        links = extract_links(response, blacklist_extensions=['.org'])
        self.assertEquals(links, ['http://tomato.com/test'])

    def test_filter_links(self):
        links = [
            'http://tomato.org/test',
            'http://tomato.com/test',
            'https://cucumber.org/tomato',
            'https://salad.org/test'
        ]
        links_filtered = filter_links(links, 'tomato\.org')
        self.assertEquals(links_filtered, ['http://tomato.org/test'])
