import csv

class Item:
    def __init__(self,name:str,price:float,quantity=0) :
        self.name = name
        self.price = price
        self.quantity = quantity


phone1= Item("jscphonev10",500,5)
phone1.broken_phones = 1
phone2 = Item("jscphonev10",500,5)
