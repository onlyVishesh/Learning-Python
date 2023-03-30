
class Train:
    def __init__(self,name,fare ,seats):
        self.name = name
        self.fare = fare
        self.seats = list(range(1,seats+1))


    def book(self,name,age):
        if len(self.seats) > 0 :
            print(f"{name} seat has been booked in train {self.name} and your seat no. is {self.seats[-1]}")
            self.seats.pop()
        else:
            print(f"Sorry, we can't book your seat")


    def getFare(self):
        print(f"fare of train {self.name} is Rs. {self.fare}")


    def getStatus(self):
        print(f"Available seats are {self.seats}")


    def cancel(self,name,age,seatno):
            self.seats.append(seatno)
            self.seats.sort()
            print(f"{name}, your ticket has been cancelled")

def main1():

    intercity = Train("Rajdahini express",200,20)
    intercity.getFare()
    intercity.getStatus()
    intercity.book("Vishesh",19)
    intercity.getStatus()

    interstate = Train("Express",490,1)
    interstate.getFare()
    interstate.getStatus()
    interstate.book("Mohit",50)
    interstate.getStatus()

    intercity.book("Vishesh1",16)
    intercity.book("Vishesh2",15)
    intercity.book("Vishesh3",14)
    intercity.book("Vishesh4",13)
    intercity.book("Vishesh5",12)

    intercity.cancel("Vishesh",19,20)
    intercity.cancel('Vishesh3',14,17)
    intercity.getStatus()


class calculator:

    def __init__(self,num):
        self.num = num


    def sq(self):
        print(f"the square of {self.num} is {self.num**2}")


    def cube(self):
        print(f"the square of {self.num} is {self.num**3}")


    def sqrt(self):
        print(f"the square of {self.num} is {self.num**.5}")

    @staticmethod # used when we don't need self argument
    def greetings():
        print("Hello, nice to meet you")

def main2():
    num1 = calculator(9)
    num1.greetings()
    num1.sq()
    num1.cube()
    num1.sqrt()


if __name__ == "__main__":
    main1()