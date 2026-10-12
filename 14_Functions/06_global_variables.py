def sum(a,b):
    c = a+b
    global x
    x=0
    print('The summing ')
    return c

x = 4
print(sum(2,2))
print(x)