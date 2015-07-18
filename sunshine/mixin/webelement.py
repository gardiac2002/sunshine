import six
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class SunnyWebElementMixin(object):
    """

    """
    def __repr__(self):
        return self.html

    def __len__(self):
        return len(self.__to_html(pretty=True))

    def __to_html(self, pretty):

        if six.PY3:
            outer_html = super().get_attribute('outerHTML')
        else:
            outer_html = super(SunnyWebElementMixin, self).get_attribute('outerHTML')

        soup = BeautifulSoup(outer_html, 'html.parser')
        if pretty:
            return soup.prettify()
        else:
            return str(soup)

    @property
    def html(self):
        """
        """
        return self.__to_html(pretty=True)

    def press_enter(self):
        """
        Press ENTER / RETURN key on element.
        """
        if six.PY3:
            return super().send_keys(Keys.RETURN)
        else:
            return super(SunnyWebElementMixin, self).send_keys(Keys.RETURN)
