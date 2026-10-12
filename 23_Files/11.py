#Count the number of characters in file 


with open("Harry.txt","r")as f1:
    content  = f1.read()

    print(len(content)) 