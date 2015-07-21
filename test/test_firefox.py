__author__ = 'sen'

import unittest

from selenium.common.exceptions import TimeoutException

from test.test_server import TestWebServer
from sunshine.ext.display import Display

class TestFirefoxCreation(unittest.TestCase):

    def test_context_manager(self):
        from sunshine import webdriver

        with TestWebServer(), webdriver.Firefox(visible=False) as firefox:
            firefox.get('localhost:5000')
            title = firefox.title.lower()
            self.assertIn('test', title)


class TestFirefoxFunctionality(unittest.TestCase):

    LOCALTEST_URL = 'localhost:5000'

    @classmethod
    def setUpClass(cls):
        cls.webserver = TestWebServer()
        cls.webserver.start_server()
        from sunshine import webdriver
        cls.firefox = webdriver.Firefox(visible=False)

    @classmethod
    def tearDownClass(cls):
        cls.webserver.stop_server()
        cls.firefox.quit()

    def test_get_website(self):
        self.firefox.get(self.LOCALTEST_URL)

    def test_find_element_by_id(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_id('start-of-content')

    def test_find_element_by_class_name(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_class_name('planet')
        self.assertEquals(element.tag_name, 'div')

    def test_find_element_by_css_selector(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_css_selector('li a')
        self.assertEquals(element.tag_name, 'a')

    def test_find_element_by_link_text(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_link_text('Sunshine Test Project')
        self.assertEquals(element.tag_name, 'a')

    def test_find_element_by_name(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_name('topofthepage')
        self.assertEquals(element.tag_name, 'h1')

    def test_find_element_by_tag_name(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_tag_name('head')
        self.assertEquals(element.tag_name, 'head')

    def test_find_element_by_xpath(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_xpath('.//div[@id="navigation"]')
        self.assertEquals(element.tag_name, 'div')

    def test_find_element_not_existing(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_id('not-existing-id')
        self.assertEquals(element, None)

    def test_find_element_raise_error(self):
        from sunshine import webdriver
        firefox = webdriver.Firefox(raise_exception=True, visible=False)

        with self.assertRaises(TimeoutException):
            firefox.get(self.LOCALTEST_URL)
            firefox.find_element_by_id('not-existing-id')
        firefox.quit()

if __name__ == '__main__':
    unittest.main()
