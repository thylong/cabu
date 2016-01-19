# -*- coding: utf-8 -*-

import re

try:
    from bs4 import BeautifulSoup, SoupStrainer
except Exception:  # pragma: no cover
    from BeautifulSoup import BeautifulSoup, SoupStrainer

from cabu.exceptions import LinkExtractorException


def extract_links(response_content, unique=False, blacklist_domains=[],
                  whitelist_domains=[], regex=None, zen_path=None,
                  blacklist_extensions=[], whitelist_extensions=[]):
    """Extract links from a response content.

    Args:
        response_content (str): The HTML page received in a Response Object.
        unique (bool): A parameter defining if the list can contain duplicates.
                       Defaults to False.
        blacklist_domains (list): List of domains to exclude from the result.
        whitelist_domains (list): List of domains to include from the result.
        regex (list): A regular expression filter on the link.
                      Defaults to None.
        zen_path (list): A selector to restrict the XPath to parse with bs4.

    Returns:
        links (list): A list of extracted and filtered links.
    """

    if any([item in blacklist_domains for item in whitelist_domains]) \
       or any([item in blacklist_extensions for item in whitelist_extensions]):
        raise LinkExtractorException('blacklist_domains and whitelist_domains '
                                     'can`t contain common value(s).')

    soup = BeautifulSoup(
        response_content, "html.parser", parse_only=SoupStrainer('a')
    )
    links = [a.text for a in soup]

    if unique:
        links = list(set(links))

    if regex:
        links = filter_links(links, regex)

    if whitelist_domains:
        for domn in whitelist_domains:
            links = filter_links(links, domn.replace('.', '\.'), include=True)

    if blacklist_domains:
        for domn in blacklist_domains:
            links = filter_links(links, domn.replace('.', '\.'), include=False)

    if whitelist_extensions:
        for ext in whitelist_extensions:
            links = filter_links(links, ext.replace('.', '\.'), include=True)

    if blacklist_extensions:
        for ext in blacklist_extensions:
            links = filter_links(links, ext.replace('.', '\.'), include=False)

    return links


def filter_links(links, regex, include=True):
    """Filter a list of links based on the given params.

    Args:
        regex (str): A regular expression filter to apply on every links.
        include (bool): Determines if the regex exclude or include matchs.

    Returns:
        links_filtered (list): The list filtered according to the arguments.
    """
    links_filtered = []
    for link in links:
        if re.search(regex, link) and include:  # whitelist case
            links_filtered.append(link)
        elif not re.search(regex, link) and not include:  # blacklist case
            links_filtered.append(link)
    return links_filtered
