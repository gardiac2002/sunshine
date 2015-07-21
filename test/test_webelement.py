__author__ = 'sen'

import unittest

from test.test_server import TestWebServer

from pyvirtualdisplay import Display

class TestWebElement(unittest.TestCase):

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

    def test_to_html(self):
        self.firefox.get(self.LOCALTEST_URL)
        element = self.firefox.find_element_by_tag_name('h1')
        html_str = element.html
        self.assertIn('h1', html_str)
        self.assertIn('big_header', html_str)
        self.assertIn('Sunshine', html_str)
        self.assertIn('</a>', html_str)
