import abc

class ObserverBase(abc.ABC):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def update(self):
        print("{0} report : {1}".format(self.name, self.subject.state))

class Observer_1(ObserverBase):
    pass

class Observer_2(ObserverBase):
    pass

class Subject(object):
    def __init__(self):
        self.state = ""
        self.observer_list = []

    def attach(self, o):
        self.observer_list.append(o)

    def detach(self, o):
        self.observer_list.remove(o)

    def notify(self):
        for observer in self.observer_list:
            observer.update()

if __name__ == '__main__':
    s = Subject()
    o1 = Observer_1("observer 1", s)
    o2 = Observer_1("observer 2", s)
    s.attach(o1)
    s.attach(o2)
    s.state = "earthquike happening ..."
    s.notify()