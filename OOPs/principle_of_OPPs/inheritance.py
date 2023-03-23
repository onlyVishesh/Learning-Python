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


def main1():
    class Phone(Item):
        all = []

        def __init__(self, name: str, price: float, quantity=0, brokenPhone=0):
            assert price >= 0, f"Price - {price} is not greater than zero"
            assert quantity >= 0, f"Quantity - {quantity} is not greater than zero"
            assert brokenPhone >= 0, f"Broken phone - {brokenPhone} is not greater than zero"

            self.name = name
            self.price = price
            self.quantity = quantity
            self.brokenPhone = brokenPhone

            Phone.all.append(self)

    phone1 = Phone("Iphone 10", 83000, 5, 1)
    print(phone1.calculateTotalPrice())
    phone2 = Phone("Iphone 11", 85000, 4, 2)


def main2():    # Using super function in main1() function
    class Phone(Item):
        all = []

        def __init__(self, name: str, price: float, quantity=0, brokenPhone=0):
            # Calling super fn to have access to all attributes / methods of parents class
            super().__init__(
                name, price, quantity
            )

            assert brokenPhone >= 0, f"Broken phone - {brokenPhone} is not greater than zero"

            self.brokenPhone = brokenPhone

            Phone.all.append(self)

    phone1 = Phone("Iphone 10", 83000, 5, 1)
    print(phone1.calculateTotalPrice())
    phone2 = Phone("Iphone 11", 85000, 4, 2)


def main3():
    class Phone(Item):
        def __init__(self, name: str, price: float, quantity=0, brokenPhone=0):
            # Calling super fn to have access to all attributes / methods of parents class
            super().__init__(
                name, price, quantity
            )

            assert brokenPhone >= 0, f"Broken phone - {brokenPhone} is not greater than zero"

            self.brokenPhone = brokenPhone

    phone1 = Phone("Iphone 10", 83000, 5, 1)
    print(Item.all)
    print(phone1.all)


if __name__ == "__main__":
    main3()
