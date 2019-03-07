from threading import RLock

class Singleton(object):
    _instance = None
    lock = RLock()
    def __new__(cls, *args, **kwargs):
        cls.lock.acquire()
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        cls.lock.release()
        return cls._instance

t1 = Singleton()
t2 = Singleton()

print(t1)
print(t2)

def singleton(cls):
    instance = {}
    def wrapper_class(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper_class

@singleton
class Test(object):
    def __init__(self, n):
        self.n = n

t3 = Test(1)
t4 = Test(2)
print(t3)
print(t4)
