# It is a concept op OPPs that only shows necessary attributes and hides unnecessary info

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
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 15:
            raise Exception("The name is too long")
        else:
            self.__name = value


    def calculateTotalPrice(self):
        return self.price * self.quantity

    def afterDiscount(self):
        return self.price * self.quantity * self.payRate

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


item1 = Item("MyItem",750,6)

item1.send_email()