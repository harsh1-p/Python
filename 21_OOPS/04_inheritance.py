class Animal:                   #Parent Class
    def eat(self):
        print("Eating")

class Dog(Animal):              #Child class
    def bark(self):
        print("Woof")


d = Dog()                       #Object
d.eat()
d.bark()
