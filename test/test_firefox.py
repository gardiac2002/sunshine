__author__ = 'sen'

import unittest

class TestFirefoxCreation(unittest.TestCase):

    def test_context_manager(self):
        from pyvirtualdisplay import Display
        from sunshine import webdriver

        display = Display(visible=False, size=(1024, 768))
        display.start()

        with webdriver.Firefox() as firefox:
            firefox.get('nytimes.com')
            title = firefox.title.lower()
            self.assertIn('times', title)

        display.stop()



class TestFirefoxFunctionality(unittest.TestCase):

    def setUp(self):
        from sunshine import webdriver
        from pyvirtualdisplay import Display
        self.display = Display(visible=False, size=(1024, 768))
        self.display.start()
        self.firefox = webdriver.Firefox()

    def tearDown(self):
        self.firefox.quit()
        self.display.stop()

    def test_get_website(self):
        self.firefox.get('derstandard.at')

    def test_find_element_by_id(self):
        self.firefox.get('github.com')
        element = self.firefox.find_element_by_id('start-of-content')

    def test_find_element_by_class_name(self):
        self.firefox.get('lemonde.fr')
        element = self.firefox.find_element_by_class_name('accueil')
        self.assertEquals(element.tag_name, 'body')

    def test_find_element_by_css_selector(self):
        self.firefox.get('xkcd.com')
        element = self.firefox.find_element_by_css_selector('li a')
        self.assertEquals(element.tag_name, 'a')

    def test_find_element_by_link_text(self):
        self.firefox.get('bitbucket.com')
        element = self.firefox.find_element_by_link_text('Log in')
        self.assertEquals(element.tag_name, 'a')

    def test_find_element_by_name(self):
        self.firefox.get('slashdot.org')
        element = self.firefox.find_element_by_name('topothepage')
        self.assertEquals(element.tag_name, 'a')

    def test_find_element_by_tag_name(self):
        self.firefox.get('slashdot.org')
        element = self.firefox.find_element_by_tag_name('head')
        self.assertEquals(element.tag_name, 'head')

    def test_find_element_by_xpath(self):
        self.firefox.get('xkcd.com')
        element = self.firefox.find_element_by_xpath('.//div[@id="topContainer"]')
        text = element.text.lower()
        self.assertIn('comic', text)

if __name__ == '__main__':
    unittest.main()
