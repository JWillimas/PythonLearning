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
