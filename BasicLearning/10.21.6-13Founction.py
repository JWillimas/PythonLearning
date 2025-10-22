# 6-xaegs
# def multiply(*numbers):
#     # use plural name here to indicate that
#     # this is a collection of values
#     # and one asterisk indicates '*numbers' is a tuple
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# 7-args
# when we use double asterisks before a parameter
# it allows us to pass a variable number of keyword arguments
# python will automatically pack these arguments into a dictionary

# def user_info(**user):
#     print(user)


# user_info(id=1, First_name="Woody", Last_name="Allen", age=70)


# 8-Scope
# Scope refers to the region of the code where the variable is defined
# know the differences between local and global variables
# message = "a"
# def greet():
#     message = "b"
# print(f"{message}")

# 9-debugging
# Press F9 to add breakpoint
# Press F10 to next line
# Press F11 to step into function
# Press Shift+F11 to step out of function
# Press Shift+F5 to stop debugging

# 10-VS-CodeTricks

# Move cursor to line start: Home
# Move cursor to line end: End
# Move cursor to File start:ctrl+Home

# Select line Press: Alt+Down/Up to Move line up/down
# Duplicatie line: Shift+Alt+Down/Up

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(2, 3, 4, 5))

# 12-Exercise
# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 != 0:
#         print("Fizz")
#     elif input % 3 != 0 and input % 5 == 0:
#         print("Buzz")
#     elif input % 3 == 0 and input % 5 == 0:
#         print("Fizz\nbuzz")
#     else:
#         print(f"{input}")


# Num = input("Please input your num: ")
# fizz_buzz(int(Num))

# 13-Solution
# The "if "syntax is confirm sentence by sentence in order of input
# Because if the last line is false ,it will go next;

def Fizz_Buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz\nBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input


Num = input("\nPlease input your num:\n")
print(Fizz_Buzz(int(Num)), "\n")
