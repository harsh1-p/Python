try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))

    c = a + b
    print("The sum is ",c)

except Exception as e:
    print(e)

finally:
    print("End")