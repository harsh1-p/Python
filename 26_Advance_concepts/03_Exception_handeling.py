while True:
    try:
        a = int(input('Enter a number : '))
        b = int(input('Enter a number : '))

        print(f"The sum is {a + b}")

    except Exception as e:
        print("Error",e)


