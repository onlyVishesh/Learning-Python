'''

classes is a user define datatype

'''

class Student:
   
   def __init__ (self,name,house):  # define to initialize the contents of an object from a class
      self.name = name
      self.house = house


def main():
   student = get_student2()
   print(f"{student.name} from {student.house}")


def get_student1():
   student = Student() # creating object/instance
   student.name = input("Name : ")
   student.house = input("House : ")
   return student

def get_student2():
   name = input("Name : ")
   house = input("House : ")
   return Student(name,house)

if __name__ == "__main__":
   main()


# class School:

#    schoolname = 'MPS' #class variable
#    def __init__(self,name,Class,admno,fathername):
#       self.name = name #instance variable
#       self.Class = Class
#       self.admno = admno
#       self.fathername = fathername

#    def active(self):
#       print(f'{self.name} is a active student')
#       return self

#    def lazy(self):
#       print(f'{self.name} is a lazy student')
#       return self#

# student_1 = School((input('Enter Your Name:   ')), (int(input('Enter Your Class:   '))),(int(input('Enter Your Admno.:   '))) , (input('Enter Your Father Name:   ')))
# print(f'''

# {student_1.name}
# {student_1.Class}
# {student_1.admno}
# {student_1.schoolname}
# {student_1.fathername}

# ''')
      
# student_1.lazy() #if we don't use with print none will also not print
# student_1.active()
# print(student_1.lazy()) #if we use with print it will also print none but this will not work after adding return self in function
# student_1.active().lazy() # this will do the work of above single statement and also work quickly