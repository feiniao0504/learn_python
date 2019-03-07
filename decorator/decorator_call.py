import time
class Decorator(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        t1 = time.time()
        self.f()
        t2 = time.time()
        print("consume time : {0}".format(t2 - t1))

#Decorator(test) 
@Decorator
def test():
    time.sleep(2)

test()