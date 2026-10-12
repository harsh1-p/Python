#Converting lowercase to upppercase 

with open("Harry.txt","r")as f1:
    content  = f1.read()
    uppercase = content.upper()
    
with open("Harry.txt","w") as f2:
    f2.write(uppercase)

    