class student:
    college = "GHRISTU"                         #class attribue

    def __init__(self,name,age,college):
        self.name = name                        #Instance attribute
        self.age = age                          #Instance attribute
        self.college = college                  #Instance attribute

e1 = student("Harsh",20,"IIMA")
print(e1.name)
print(e1.age)                                   #Here we print 3 instance attribute and suppose college was not print it would have printed GHRISTU
print(e1.college)

print(student.college)                          #Here we print class attribute



        