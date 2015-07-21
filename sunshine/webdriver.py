__author__ = 'sen'
import doctest
from selenium import webdriver

from sunshine.mixin import browser

class Firefox(browser.SunnyFirefoxMixin, webdriver.Firefox):
    """

    Sunshine's Firefox class supports context managers::

        >>> from sunshine import webdriver
        >>> with webdriver.Firefox(visible=False) as firefox:
        ...     firefox.get('nytimes.com')
        ...     title = firefox.title.lower()
        ...     'times' in title
        True

    * The __init__ function (url)
    * finds with wait
    """
    pass

if __name__ == '__main__':
    doctest.testmod()