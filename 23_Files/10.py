#Copying two files  


with open("Harry.txt","r") as f1:
    content = f1.read()

with open ("harsh.txt","w") as f2:
    f2.write(content)
    