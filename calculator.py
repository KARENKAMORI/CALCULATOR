import time
import os

def main():
    print("**********CALCULATOR**********")
    while True:
        print("CHOOSE FROM THE OPTIONS BELOW:")
        print("1). ADDITION.")
        print("2). SUBTRACTION.")
        print("3). MULTIPLICATION.")
        print("4). DIVISION.")
        print("5). EXIT")

        choice = int(input("Enter Choice: "))

    # switch case
        match choice:
            case 1:
                add()
            case 2:
                sub()
            case 3:
                mult()
            case 4:
                div()
            case 5:
                exit()
        next()

def user_input():
    # use of the try except block for error checking
    while True:
        try:
            a = int(input("Enter first number: "))
        except ValueError:
            pass
        else:
            break

    while True:
        try:
            b = int(input("Enter second number: "))
        except ValueError:
            pass
        else:
            break

    return a, b

# a function that waits for one second and clears the screen
def next():
    time.sleep(1)
    os.system("cls")

# Addition function
def add():
    next()
    print("*****ADDITION*****")
    x,y = user_input()
    print(f"{x} + {y} = {x+y}")

# Subtraction function
def sub():
    next()
    print("*****SUBTRACTION*****")
    x,y = user_input()
    print(f"{x} - {y} = {x-y}")

# Multiplication function
def mult():
    next()
    print("*****MULTIPLICATION*****")
    x,y = user_input()
    print(f"{x} * {y} = {x*y}")

# Division function
def div():
    next()
    print("*****DIVISION*****")
    x,y = user_input()
    print(f"{x} / {y} = {x/y}")

if __name__ == "__main__":
    main()