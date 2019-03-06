#_*_coding:utf-8_*_
__author__ = 'zys'

import threading
import time

def addNum():
    global num
    print("counting num ... {0}".format(num))
    time.sleep(1)
    lock.acquire()
    num += 1
    lock.release()

num = 0
lock = threading.Lock()
thread_list = []

for i in range(100):
    t = threading.Thread(target=addNum, args=())
    thread_list.append(t)
    t.start()

for item in thread_list:
    item.join()

print(num)

