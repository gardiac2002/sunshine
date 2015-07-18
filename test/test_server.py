import time
from multiprocessing import Process

from .server import app

class TestWebServer:
    """
    Helper class to manage your flask test server.
    """

    def __init__(self, port=5000, startup_wait=0.25):
        """
        """
        self.server = None
        self.port = port
        self.startup_wait = startup_wait

    def __enter__(self):
        """
        Convenience function for the 'with' statement.
        :return:
        """
        self.start_server()
        time.sleep(self.startup_wait)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Convenience function for the 'with' statement.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.stop_server()

    def start_server(self):
        """
        Start your test Flask server.
        :return:
        """
        run = lambda port: app.run()
        self.server = Process(target=run, args=(self.port,))
        time.sleep(self.startup_wait)
        self.server.start()

    def stop_server(self):
        """
        Stop your test Flask server.
        :return:
        """
        if self.server:
            self.server.terminate()
            self.server.join()
