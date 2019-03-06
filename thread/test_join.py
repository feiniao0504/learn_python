#_*_coding:utf-8_*_
__author__ = 'zys'

import threading
import time

def count(n):
    print("counting number: {0}".format(n))
    time.sleep(3)
    print("counting end ...")

t1 = threading.Thread(target=count, args=(1, ))
t2 = threading.Thread(target=count, args=(2, ))

t1.start()
t1.join()
t2.start()
t2.join()