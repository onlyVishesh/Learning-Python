def main1():
    class Item:
        pass

    item1 = Item()
    item1.name = "Phone"
    item1.price = 15000
    item1.quantity = 200

    print(
        f"The name of the item is {item1.name} and its price is {item1.price} and we need a quantity of {item1.quantity}")


def main2():
    class Item:
        def calculateTotalPrice(self, x, y):
            return x*y

    item1 = Item()
    item1.name = "Phone"
    item1.price = 15000
    item1.quantity = 200

    item2 = Item()
    item2.name = "Laptop"
    item2.price = 55000
    item2.quantity = 50

    print(
        f"Total cost for item {item1.name} is {item1.calculateTotalPrice(item1.price,item1.quantity)}")
    print(
        f"Total cost for item {item2.name} is {item2.calculateTotalPrice(item2.price,item2.quantity)}")


def main3():
    class Item:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def calculateTotalPrice(self):
            return self.price * self.quantity

    item1 = Item("Phone", 15000, 200)
    item2 = Item(name = "Laptop", quantity = 50, price = 55000)

    print(f"Total cost for item {item1.name} is {item1.calculateTotalPrice()}")
    print(f"Total cost for item {item2.name} is {item2.calculateTotalPrice()}")


def main4():
    class Item:
        # Giving datatype and default values to the argument
        def __init__(self, name: str, price: float, quantity=0):
            # Run Validation to the receiving arguments
            assert price >= 0, f"Price {price} is not greater than zero"
            assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
            # Assign to self object
            self.name = name
            self.price = price
            self.quantity = quantity

        def calculateTotalPrice(self):
            return self.price * self.quantity

    item1 = Item("Phone", -2432, -10)
    print(f"Total cost for item {item1.name} is {item1.calculateTotalPrice()}")


def main5():
    class Item:
        payRate = 0.8  # The pay rant after 20% discount

        # Giving datatype and default values to the argument
        def __init__(self, name: str, price: float, quantity=0):
            # Run Validation to the receiving arguments
            assert price >= 0, f"Price {price} is not greater than zero"
            assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
            # Assign to self object
            self.name = name
            self.price = price
            self.quantity = quantity

        def calculateTotalPrice(self):
            return self.price * self.quantity

        def afterDiscount(self):
            return self.price * self.quantity * self.payRate

    print(Item.payRate)

    item1 = Item("Phone", 2432, 10)
    print(item1.payRate)

    print(Item.__dict__)    # All the attributes for class level
    print(item1.__dict__)   # All the attributes for object level

    print(
        f"Total cost for item {item1.name} is {item1.calculateTotalPrice()} and after discount of {100 - Item.payRate*100}% is {item1.afterDiscount()}")

    item2 = Item("Laptop", 24000, 10)
    print(
        f"Total cost for item {item2.name} is {item2.calculateTotalPrice()} and after discount of {100 - item2.payRate*100}% is {item2.afterDiscount()}")
    
    item2.payRate = 0.7
    print(item2.payRate)
    print(
        f"Total cost for item {item2.name} is {item2.calculateTotalPrice()} and after discount of {100 - item2.payRate*100}% is {item2.afterDiscount()}")


def main6():
    class Item:
        payRate = 0.8
        all = []

        def __init__(self, name: str, price: float, quantity=0):
            assert price >= 0, f"Price {price} is not greater than zero"
            assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
            self.name = name
            self.price = price
            self.quantity = quantity

            # Action that is execute
            Item.all.append(self)

        def __repr__(self):
            return f"\nItem('{self.name}',{self.price},{self.quantity})"

    item1 = Item("Phone", 15000, 200)
    item2 = Item(name = "Laptop", quantity = 50, price = 55000)
    item3 = Item("Cable", 150, 25)
    item4 = Item("Mouse", 700, 20)
    item5 = Item("Keyboard", 1500, 10)

    # To access name of object
    # for item in Item.all:
    #     print(item.name)

    print(Item.all)

    
def main7():
    import csv
    class Item:
        payRate = 0.8
        all = []

        def __init__(self, name: str, price: float, quantity=0):
            assert price >= 0, f"Price {price} is not greater than zero"
            assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
            self.name = name
            self.price = price
            self.quantity = quantity

            # Action that is execute
            Item.all.append(self)

        def __repr__(self):
            return f"\nItem('{self.name}',{self.price},{self.quantity})"

        # To print Each instantiates
        # @classmethod
        # def instantiate_from_csv(cls):
        #     with open('OPPs2.csv','r') as f:
        #         reader = csv.DictReader(f)
        #         items = list(reader)

            # for item in items:
            #     print(item)

        @classmethod
        def instantiate_from_csv(cls):
            with open('OPPs2.csv','r') as f:
                reader = csv.DictReader(f)
                items = list(reader)


            for item in items:
                Item(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity"))
                )          

    Item.instantiate_from_csv()
    print(Item.all)


def main8():
    import csv
    class Item:
        payRate = 0.8
        all = []

        def __init__(self, name: str, price: float, quantity=0):
            assert price >= 0, f"Price {price} is not greater than zero"
            assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
            self.name = name
            self.price = price
            self.quantity = quantity

            Item.all.append(self)

        def __repr__(self):
            return f"\nItem('{self.name}',{self.price},{self.quantity})"

        @classmethod
        def instantiate_from_csv(cls):
            with open('OPPs2.csv','r') as f:
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
            if isinstance(num,float):
                return num.is_integer()
            elif isinstance(num,int):
                return True
            else:
                return False
            


    print(Item.is_integer(7))   # We can give values like 7 ,7.0 and get true and for values like 2.3,4.5 it gives false
    # Item.instantiate_from_csv()
    # print(Item.all)



 

if __name__ == "__main__":
    main8()
