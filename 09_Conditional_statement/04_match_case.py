a = int(input("Enter a number between 1-10 ,Win a lucky prize : "))

match a:
    case 1:
        print("You won a Camera")
    case 5:
        print("You won a Mobile Phone") 
    case 9:
        print("You won a Car")
    case _:
        print("Better luck next time!")
