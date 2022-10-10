import os

import logging

LOG = logging.getLogger()


def test_function():
    print("TEST DUMP 4")
    print(os.listdir())

def trigger():

    LOG.info("shape of data is : {}")
    print("TEST DONE")



