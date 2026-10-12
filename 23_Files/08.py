#Useer input and creating files and entering text 


def func():

    f = open("New.txt","w")

    content = input("Enter you text here : ")

    f.write(content)

    f.close()

func()