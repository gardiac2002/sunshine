__author__ = 'sen'

from bs4 import BeautifulSoup

def prettify_html(html_str):
    """

    :param html_str:
    :return:
    """
    soup = BeautifulSoup(html_str, 'html.parser')
    return soup.prettify()