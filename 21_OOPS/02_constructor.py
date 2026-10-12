class student:                              #Class

    def  __init__(self,name,age):           #Constructor
        self.name = name                    #object attribute
        self.age = age


s = student("Harsh",20)                     #s is object

print(s.name)
print(s.age)


class Car:

    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

c = Car("Toyota",1000000)

print(c.brand)
print(c.price)


        