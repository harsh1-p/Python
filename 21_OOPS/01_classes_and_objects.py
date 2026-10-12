class Student:                  #Class
    college = "GHRISTU"         #Class Variable 

    def get_name(self):         #Method
        return "Harsh"

s = Student()                   #s is object here
print(s.get_name())             #Calling a method using object
print(s.college)                #Printing class varaiable using an object 



class Car:
    brand = "Toyota"

    def get_price(self):
        return 50000000

c = Car()
print(c.get_price())


class Employee:
    comapny = "Google"

    def get_details(self):
        return "SDE"

e1 = Employee()
print(e1.get_details())

e2 = Employee()
print(e2.get_details())