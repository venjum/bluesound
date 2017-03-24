# Bluesound Python 3 API

Bluesound API for for controlling a Bluesound player.
see: http://www.bluesound.com

## Install (program is in beta, must install with github address)
pip3 install git+https://github.com/venjum/bluesound.git

## Example of usage:

### Make a subscription handler:
def handelTitle1(new_title):
    print(new_title)

title1 = SubscriptionObject(['status', 'title1'], handelTitle1)

### Or use some of the predefined subscription objects, but remember to set callback
from bluesound_subscription_objects import secondsInTrack

def handelSecondsInTrack(sec):
    print(sec)

secondsInTrack.setCallback(handelSecondsInTrack)

### Then initiate and start Bluesound thread
bluos = Bluesound("192.168.1.87", 1.0, set([title1, secondsInTrack]))
bluos.start()

### Use the API
bluos.skip()

### When stopping application, remember to stop the thread as well.
bluos.stop()
