"""
Bluesound Control
This is the main module for the Bluesound API.
The application can start up this module and get notified when it's subscribed values are updated.

Example of usage:
Start service:
    bluesound = Bluesound("192.168.1.87", 1.0, subscription_list)
    bluesound.start()

Stop service:
    bluesound.stop()

"""

import threading
from bluesound_api import BluesoundApi


class Bluesound(BluesoundApi):
    """
    Main Bluesound class that is meant for application usage
    This class will start a thread that will continually read players status through given IP
    """
    def __init__(self, ip_address, request_delay, subscribe_list=set()):
        """
        Initialize Bluesound class

        Arguments:
            ip_address: IP address to your Bluesound player.
            request_delay: Seconds between each status check in floating point number.
            subscribe_list: Set of SubscriptionObject that will be notified if it's value is updated.
        """
        super(Bluesound, self).__init__(ip_address)
        self._request_delay = request_delay
        self._subscribe_list = subscribe_list
        self._thread = threading.Thread(target=self.run, name=self.__class__.__name__+"_thread")
        self._stop_event = threading.Event()
        self._read_status = threading.Event()
        self._player_status = {}

    def start(self):
        """
        Start run thread
        """
        self._thread.start()

    def stop(self):
        """
        Stop run thread
        """
        self._stop_event.set()
        if self._thread.is_alive():
            self._thread.join()

    def readStatusNow(self):
        self._read_status.set()

    def run(self):
        """
        Function that is executed in thread
        Check players status and notify if there are any changes for values in subscription list.
        """
        while True:
            if self._read_status.wait(self._request_delay):
                self._read_status.clear()

            self._player_status['status'] = self.getStatus()

            # For the moment not used. Most of attributes is found in status. Maybe sync status is used for finding players.
            # self._player_status['SyncStatus'] = self.getSyncStatus()

            for object in self._subscribe_list:
                object.updateValue(self._player_status)

            if self._stop_event.is_set():
                break
