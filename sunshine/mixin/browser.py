__author__ = 'sen'

import doctest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sunshine.webelement.webelement import WebElement


class SunnyFirefoxMixin:
    """

    """
    def __enter__(self):
        self.current_browser = self.__class__()
        return self.current_browser

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current_browser.quit()

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
        super().get(url)

    def __find_element(self, selector, wait):
        waiter_obj = WebDriverWait(super(), wait)
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