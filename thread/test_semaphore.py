#_*_coding:utf-8_*_
__author__ = 'zys'

import threading
import time

def count(n):
    print("counting number: {0}".format(n))
    semaphore.acquire()
    time.sleep(1)
    semaphore.release()
    print("counting end ...")

semaphore = threading.BoundedSemaphore(3)

for i in range(5):
    t = threading.Thread(target=count, args=[i, ])
    t.start()
