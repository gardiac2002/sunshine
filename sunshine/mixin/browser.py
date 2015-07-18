__author__ = 'sen'

import doctest
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
import six

from sunshine.webelement.webelement import WebElement


class SunnyFirefoxMixin(object):
    """

    """
    def __enter__(self):
        self.current_browser = self.__class__()
        return self.current_browser

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        if self.current_browser:
            self.current_browser.quit()

    def __repr__(self):
        s = '<sunshine $name object at "$website">'
        template = string.Template(s)
        settings = {'name':self.name, 'website':self.current_url}
        return template.substitute(settings)

    def get(self, url):
        """
        Go to a website
        :param url: The URL of the website

        Usage::

            >>> from sunshine import webdriver
            >>> browser = webdriver.Firefox()
            >>> browser.get('github.com')
            >>> browser.quit()
        """
        if not url.startswith('http://'):
            url = 'http://' + url

        if six.PY3:
            super().get(url)
        else:
            super(SunnyFirefoxMixin, self).get(url)

    def __find_element(self, selector, wait):

        if six.PY3:
            super_obj = super()
        else:
            super_obj = super(SunnyFirefoxMixin, self)

        waiter_obj = WebDriverWait(super_obj, wait)
        condition = EC.presence_of_element_located(selector)
        element = waiter_obj.until(condition)
        return WebElement(parent=element.parent, id_=element.id)

    def find_element_by_id(self, _id, wait=10):
        """
        Search and find an element by id.
        :param _id:
        :param wait: Time to wait before stopping (default: 10 seconds)
        :return: the found element

        Usage::

            >>> from sunshine import webdriver
            >>> browser = webdriver.Firefox()
            >>> browser.get('github.com')
            >>> element = browser.find_element_by_id('start-of-content')
            >>> browser.quit()
        """
        selector = (By.ID, _id)
        return self.__find_element(selector, wait=wait)

    def find_element_by_class_name(self, name, wait=10):
        """

        :param class_name:
        :param wait:
        :return:
        """
        selector = (By.CLASS_NAME, name)
        return self.__find_element(selector, wait=wait)

    def find_element_by_css_selector(self, css_selector, wait=10):
        """

        :param css_selector:
        :param wait:
        :return:
        """
        selector = (By.CSS_SELECTOR, css_selector)
        return self.__find_element(selector, wait=wait)

    def find_element_by_link_text(self, link_text, wait=10):
        """

        :param link_text:
        :param wait:
        :return:
        """
        selector = (By.LINK_TEXT, link_text)
        return self.__find_element(selector, wait=wait)

    def find_element_by_name(self, name, wait=10):
        """

        :param name:
        :param wait:
        :return:
        """
        selector = (By.NAME, name)
        return self.__find_element(selector, wait=wait)

    def find_element_by_partial_link_text(self, link_text, wait=10):
        """

        :param link_text:
        :param wait:
        :return:
        """
        selector = (By.LINK_TEXT, link_text)
        return self.__find_element(selector, wait=wait)

    def find_element_by_tag_name(self, tag_name, wait=10):
        """

        :param tag_name:
        :param wait:
        :return:
        """
        selector = (By.TAG_NAME, tag_name)
        return self.__find_element(selector, wait=wait)

    def find_element_by_xpath(self, xpath, wait=10):
        """

        :param xpath:
        :param wait:
        :return:
        """
        selector = (By.XPATH, xpath)
        return self.__find_element(selector, wait=wait)


if __name__ == '__main__':
    doctest.testmod()