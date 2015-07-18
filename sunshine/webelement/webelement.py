__author__ = 'sen'

import six

from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement

from sunshine.mixin import webelement

class WebElement(webelement.SunnyWebElementMixin, SeleniumWebElement):
    """

    """
    def __init__(self, parent, id_):
        if six.PY3:
            super().__init__(parent, id_)
        else:
            super(WebElement, self).__init__(parent, id_)