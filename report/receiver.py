import os, json, sys

class Receiver(object):
    def __init__(self, **kwargs):
        self.user = kwargs.get('user', '')
        self.email = kwargs.get('email', '')
        self.phone = kwargs.get('phone', '')