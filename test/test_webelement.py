__author__ = 'sen'

import unittest

from test.test_server import TestWebServer

class TestWebElement(unittest.TestCase):

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

    def test_to_html(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_tag_name('h1')
        html_str = element.html
        self.assertIn('h1', html_str)
        self.assertIn('big_header', html_str)
        self.assertIn('Sunshine', html_str)
        self.assertIn('</a>', html_str)
