#_*_coding:utf-8_*_
__author__ = 'zys'

import threading

def hello():
    print("hello ...")

tt = threading.Timer(1, hello)
tt.start()