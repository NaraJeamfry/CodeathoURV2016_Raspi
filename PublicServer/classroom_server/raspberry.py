
import random


def test_connection(ip):
    print "Trying to connect to %s..." % ip

    print "Fake connection is successful!"

    return random.randint(0, 1)


def get_status(ip, property):
    print "Trying to connect to %s..." % ip

    print "Fake connection is successful!"

    return "Connected"