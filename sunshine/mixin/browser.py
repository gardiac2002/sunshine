__author__ = 'sen'

import doctest
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import six

from sunshine.webelement.webelement import WebElement
from sunshine.ext.display import Display


class SunnyFirefoxMixin(object):
    """

    """
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None, raise_exception=False,
                 visible=True):
        """
        :param firefox_profile:
        :param firefox_binary:
        :param timeout:
        :param capabilities:
        :param proxy:
        :param raise_exception:
        :param invisible:
        :return:
        """
        self.display = None
        self.visible = visible
        if not visible:
            self.display = Display(visible=visible)
            self.display.start()

        if six.PY3:
            super().__init__(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                             timeout=timeout, capabilities=capabilities, proxy=proxy)
        else:
            super(SunnyFirefoxMixin, self).__init__(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                                                    timeout=timeout, capabilities=capabilities, proxy=proxy)
        self.raise_exception = raise_exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if six.PY3:
            super().quit()
        else:
            super(SunnyFirefoxMixin, self).quit()
        if self.display:
            self.display.stop()

    def __repr__(self):
        s = '<sunshine $name object at "$website">'
        template = string.Template(s)
        settings = {'name':self.name, 'website':self.current_url}
        return template.substitute(settings)

    def quit(self):
        if six.PY3:
            super().quit()
        else:
            super(SunnyFirefoxMixin, self).quit()

        if self.display:
            self.display.stop()

    def get(self, url):
        """
        Go to a website
        :param url: The URL of the website

        Usage::

            >>> from sunshine import webdriver
            >>> browser = webdriver.Firefox(visible=False)
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

        try:
            waiter_obj = WebDriverWait(super_obj, wait)
            condition = EC.presence_of_element_located(selector)
            element = waiter_obj.until(condition)
            found_element = WebElement(parent=element.parent, id_=element.id)
        except TimeoutException as error:
            if self.raise_exception:
                raise TimeoutException(error.msg)
            found_element = None
        return found_element

    def find_element_by_id(self, _id, wait=5):
        """
        Search and find an element by id.
        :param _id:
        :param wait: Time to wait before stopping (default: 10 seconds)
        :return: the found element

        Usage::

            >>> from sunshine import webdriver
            >>> browser = webdriver.Firefox(visible=False)
            >>> browser.get('github.com')
            >>> element = browser.find_element_by_id('start-of-content')
            >>> browser.quit()
        """
        selector = (By.ID, _id)
        return self.__find_element(selector, wait=wait)

    def find_element_by_class_name(self, name, wait=5):
        """

        :param class_name:
        :param wait:
        :return:
        """
        selector = (By.CLASS_NAME, name)
        return self.__find_element(selector, wait=wait)

    def find_element_by_css_selector(self, css_selector, wait=5):
        """

        :param css_selector:
        :param wait:
        :return:
        """
        selector = (By.CSS_SELECTOR, css_selector)
        return self.__find_element(selector, wait=wait)

    def find_element_by_link_text(self, link_text, wait=5):
        """

        :param link_text:
        :param wait:
        :return:
        """
        selector = (By.LINK_TEXT, link_text)
        return self.__find_element(selector, wait=wait)

    def find_element_by_name(self, name, wait=5):
        """

        :param name:
        :param wait:
        :return:
        """
        selector = (By.NAME, name)
        return self.__find_element(selector, wait=wait)

    def find_element_by_partial_link_text(self, link_text, wait=5):
        """

        :param link_text:
        :param wait:
        :return:
        """
        selector = (By.LINK_TEXT, link_text)
        return self.__find_element(selector, wait=wait)

    def find_element_by_tag_name(self, tag_name, wait=5):
        """

        :param tag_name:
        :param wait:
        :return:
        """
        selector = (By.TAG_NAME, tag_name)
        return self.__find_element(selector, wait=wait)

    def find_element_by_xpath(self, xpath, wait=5):
        """

        :param xpath:
        :param wait:
        :return:
        """
        selector = (By.XPATH, xpath)
        return self.__find_element(selector, wait=wait)


if __name__ == '__main__':
    doctest.testmod()