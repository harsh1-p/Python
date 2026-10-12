#Print the reverse order of lines fro file 


with open("Harry.txt","r") as f:
    content = f.readlines()

for lines in content[::-1]:
    print(lines,end = "")
