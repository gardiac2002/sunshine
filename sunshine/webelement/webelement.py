__author__ = 'sen'

from selenium.webdriver.remote.webelement import WebElement

from sunshine.mixin import webelement


class WebElement(webelement.SunnyWebElementMixin, WebElement):
    """

    """
    def __init__(self, parent, id_):
        super().__init__(parent, id_)