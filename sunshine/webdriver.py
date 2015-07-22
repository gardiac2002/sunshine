__author__ = 'sen'
import doctest
import six

from selenium import webdriver

from sunshine.mixin import browser

class Firefox(browser.SunnyWebdriverMixin, webdriver.Firefox):
    """

    Sunshine's Firefox class supports context managers::

        >>> from sunshine import webdriver
        >>> with webdriver.Firefox(visible=False) as firefox:
        ...     firefox.get('nytimes.com')
        ...     title = firefox.title.lower()
        ...     'times' in title
        True

    * The __init__ function (url)
    * finds with wait
    """
    def __init__(self, firefox_profile=None, firefox_binary=None, timeout=30,
                 capabilities=None, proxy=None, visible=True, raise_exception=False):
        """
        """
        if six.PY3:
            super().__init__(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                             timeout=timeout, capabilities=capabilities, proxy=proxy, visible=visible,
                             raise_exception=raise_exception)
        else:
            super(Firefox, self).__init__(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                                          timeout=timeout, capabilities=capabilities, proxy=proxy, visible=visible,
                                          raise_exception=raise_exception)



class Opera(browser.SunnyWebdriverMixin, webdriver.Opera):
    """

    """
    def __init__(self, desired_capabilities=None, executable_path=None, port=0, service_log_path=None,
                 service_args=None, opera_options=None, visible=True, raise_exception=False):
        """

        :param desired_capabilities:
        :param executable_path:
        :param port:
        :param service_log_path:
        :param service_args:
        :param opera_options:
        :param visible:
        :param raise_exception:
        :return:
        """
        if six.PY3:
            super().__init__(executable_path=executable_path,
                             port=port, opera_options=opera_options,
                             service_args=service_args,
                             desired_capabilities=desired_capabilities,
                             service_log_path=service_log_path,
                             visible=visible,
                             raise_exception=raise_exception)
        else:
            super(Opera, self).__init__(executable_path=executable_path,
                                        port=port, opera_options=opera_options,
                                        service_args=service_args,
                                        desired_capabilities=desired_capabilities,
                                        service_log_path=service_log_path,
                                        visible=visible,
                                        raise_exception=raise_exception)


if __name__ == '__main__':
    print(help(Firefox))
    #doctest.testmod()