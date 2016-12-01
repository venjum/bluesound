import threading
from time import sleep
from bluesound_api import BluesoundApi


class Bluesound(BluesoundApi):
    """
    """
    def __init__(self, ip_address, request_delay):
        super(Bluesound, self).__init__(ip_address)
        self._request_delay = request_delay
        self._thread = threading.Thread(target=self.run, name=self.__class__.__name__+"_thread")
        self._stop_event = threading.Event()

    def start(self):
        """
        Start Service
        """
        self._thread.start()

    def stop(self):
        """
        Stop service
        """
        self._stop_event.set()
        if self._thread.is_alive():
            self._thread.join()

    def run(self):
        while True:
            self._sync_status = self.getSyncStatus()
            self._status = self.getStatus()

            sleep(self._request_delay)

            if self._stop_event.is_set():
                break


if __name__ == '__main__':
    try:
        test = Bluesound("192.168.1.87", 1)
        test.start()
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print(test._sync_status)
        test.stop()
