from item import Item
from phone import Phone


def main1():    # values can be change after creation of object
    # Remove @porperty method in item.py file
    Item.instantiate_from_csv()
    print(Item.all)

    item1 = Item("MyItem",50)
    item1.name = "NotMineItem"
    # we can also do it in child class but mainly we only focus on parent class in this file
    phone1 = Phone("Iphone 19",5,brokenPhone=1)
    phone1.name = "Iphone 14" 

    print(item1.name,phone1.name)


def main2():    # values can't be change after creation of object 
    # Add @porperty method in item.py file

    item1 = Item("MyItem",50)
    print(item1.price)

    # item1.price = 55  Gives - AttributeError: can't set attribute price
    
    # But we can change name by using item1._price = 55
    # So fix it we use __price as a private variable and it can't be used anywhere outside class
    item1.__price = 55 # doesn't work
    print(item1.price)


def main3():     # values can't be change after creation of object but we want it change it
    # With @porperty method in item.py file also all @name.setter method we use to price

    item1 = Item("MyItem",50)
    print(item1.name)

    item1.name = "NotMineItem"   # It is a property but also value can be change due to setter method and "NotMineItem" is the value attribute in setter fn
    print(item1.name)





if __name__ == "__main__":
    main3()
