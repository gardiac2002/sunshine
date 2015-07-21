__author__ = 'sen'

from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display

from test.test_server import TestWebServer

import unittest

class TestFirefoxCreation(unittest.TestCase):

    def test_context_manager(self):
        from pyvirtualdisplay import Display
        from sunshine import webdriver

        display = Display(visible=False, size=(1024, 768))
        display.start()

        with TestWebServer(), webdriver.Firefox() as firefox:
            firefox.get('localhost:5000')
            title = firefox.title.lower()
            self.assertIn('test', title)

        display.stop()


class TestFirefoxFunctionality(unittest.TestCase):

    LOCALTEST_URL = 'localhost:5000'

    @classmethod
    def setUpClass(cls):
        cls.webserver = TestWebServer()
        cls.webserver.start_server()

        cls.display = Display(visible=False, size=(1024, 768))
        cls.display.start()

        from sunshine import webdriver
        cls.firefox = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.display.stop()
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
        firefox = webdriver.Firefox(raise_exception=True)

        with self.assertRaises(TimeoutException):
            firefox.get(self.LOCALTEST_URL)
            firefox.find_element_by_id('not-existing-id')
        firefox.quit()

if __name__ == '__main__':
    unittest.main()
