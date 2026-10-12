#Print the last nth line 

def func(file,n):

    with open(file,'r') as f:
        line = f.readlines()
        return line[-n:]

file  = input("Enter a file name : ")
n = int(input("Enter the number of lines : "))

print(func(file,n))
