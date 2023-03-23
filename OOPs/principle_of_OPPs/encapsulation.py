# It is a mechanism restrict direct access some of the attrebutes of some parts
# @property method is used 
# We use i in price attribute

import csv

class Item:
    payRate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)


    # Making price can't be change
    
    @property
    def price(self):
        return self.__price
    
    def calculateTotalPrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        self.price -= self.price * self.payRate
    
    def applyIncrement(self, incrementValue):
        self.__price += self.price * incrementValue


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 15:
            raise Exception("The name is too long")
        else:
            self.__name = value




    @classmethod
    def instantiate_from_csv(cls):
        with open('OPPs2.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        

    # adding special method to change name from this Item class to all child classes
    def __repr__(self):
        return f"\n{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
    


item1 = Item("Pen",15,5)
# item1.price = 17 Error - AttributeError: can't set attribute 'price'

print(item1.price)
item1.applyIncrement(0.1)
print(item1.price)