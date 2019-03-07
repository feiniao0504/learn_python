import queue
import time
from threading import Thread

def producer(n):
    q.put(n)
    print("{0} in queue".format(n))

def consumer():
    while True:
        while q.qsize() > 0:
            time.sleep(0.3)
            print("{0} out queue, queue size is {1}".format(q.get(), q.qsize()))

q = queue.Queue(maxsize=5)

for i in range(100):
    t1 = Thread(target=producer, args=[i, ])
    t1.start()

t = Thread(target=consumer, args=[])
t.setDaemon(True)
t.start()
t.join(timeout=100)
