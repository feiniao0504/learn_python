import abc

class Pizza(abc.ABC):
    @abc.abstractmethod
    def price(self):
        '''price'''

    @abc.abstractmethod
    def color(self):
        '''color'''

    @abc.abstractmethod
    def size(self):
        '''size'''

class CheesePizza(Pizza):
    def price(self):
        return "CheesePizza price "

    def color(self):
        return "CheesePizza color "

    def size(self):
        return "CheesePizza size "

class BeefPizza(Pizza):
    def price(self):
        return "BeefPizza price "

    def color(self):
        return "BeefPizza color "

    def size(self):
        return "BeefPizza size "

class IFactory(abc.ABC):
    @abc.abstractmethod
    def createPizza(self):
        '''createPizza'''

class BeefPizzaFactory(IFactory):
    def createPizza(self):
        return BeefPizza()

class CheesePizzaFactory(IFactory):
    def createPizza(self):
        return CheesePizza()

if __name__ == '__main__':
    i_factory = BeefPizzaFactory()
    pizza = i_factory.createPizza()
    print(pizza.price())

    i_factory = CheesePizzaFactory()
    pizza = i_factory.createPizza()
    print(pizza.price())