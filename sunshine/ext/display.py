__author__ = 'sen'

from pyvirtualdisplay import Display as _VirtualDisplay


class Display(object):

    def __init__(self, visible=True, width=1024, height=768):
        """

        :param visible:
        :return:
        """
        screen_size = (width, height)
        self.display = _VirtualDisplay(visible=visible, size=screen_size)

    def start(self):
        """

        :return:
        """
        self.display.start()

    def stop(self):
        """

        :return:
        """
        self.display.stop()