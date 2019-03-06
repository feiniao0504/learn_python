#_*_coding:utf-8_*_
__author__ = 'zys'

import threading
import time

'''
Method 1: create directly
'''
def count(n):
    print("counting number: {0}".format(n))
    time.sleep(3)

t1 = threading.Thread(target=count, args=(1, ))
t2 = threading.Thread(target=count, args=(2, ))

t1.start()
t2.start()

'''
Method 2: inherent 
'''
class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("counting number: {0}".format(self.n))
        time.sleep(3)

t3 = MyThread(3)
t4 = MyThread(4)
t3.start()
t4.start()