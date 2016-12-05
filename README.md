# bluesound
Bluesound API for for controlling a Bluesound player. 

API written in Python 3

Example of usage:

def handelTitle1(new_title):
    print(new_title)

title1 = SubscriptionObject(['status', 'title1'], handelTitle1)

try:
    test = Bluesound("192.168.1.87", 1.0, set([title1]))
    test.start()
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    test.stop()
