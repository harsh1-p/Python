#Write a python program to count number of lines in file 

f = input('Enter you file name :')

a =  open(f,'r')
count =  0
for lines in a:
    count+=1

print(f"The number of lines are {count}")

a.close()