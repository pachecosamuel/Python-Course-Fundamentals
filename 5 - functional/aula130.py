class House:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value > 0 and isinstance(value, float):
            self.__price = value
        else:
            print("Type a valid value for price")

    @price.deleter
    def price(self):
        del self.__price

my_house = House(500000)
print(my_house.price)
my_house.price = 600000.50
print(my_house.price)