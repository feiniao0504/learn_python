from multiprocessing import Process
import time

def f(name):
    time.sleep(2)
    print("hello, {0}".format(name))

if __name__ == '__main__':
    p = Process(target=f, args=["zys",])
    p1 = Process(target=f, args=["zys",])
    p.start()
    p1.start()
    