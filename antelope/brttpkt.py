#!/usr/bin/env python

from time import sleep

from collections import deque

class Timeout(Exception): pass
class NoData(Exception): pass

get_rvals = deque()

class OrbreapThr(object):
    def __init__(self, *args, **kwargs):
        pass

    def get(self):
        try:
            return get_rvals.pop()
        except IndexError:
            sleep(99999)

    def __enter__(self, *args, **kwargs):
        return self

    def __exit__(self, *args, **kwargs):
        pass

