# 2-Handle the expection
# 3-Handing Different Exception
# If you don't handle your expecttion properly
# your program will crash

# 4-clean up
# duplication is a bad practice in programming

# Using Finally calues to release resource

# 5-The with statement
# Using shorter or cleaner way but without the finally clause
# when we using the 'with' sentence,python will use
# Finally whether we have final clause or not


# try:
#     with open(r"d:\VScodeFile\PythonLearning\A.BasicLearning\10.31Excptions.py")as file:
#         print("File opened.")
#     # If the object like 'file'
#     # Have management protocol we can use with method
#     # python will automatic called finally method
#     age = int(input("Age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError) as ex:
#     # We can optionally define a variable
#     # that will include the details about the exception

#     if isinstance(ex, ValueError):
#         print("You didn't enter a valid age")
#         print(ex)  # Value error
#         print(type(ex))
#     elif isinstance(ex, ZeroDivisionError):
#         print("You can't enter a Zero value")

# else:
#     print("No exception were thrown.")

# 6-Raising Exception:
# raise lets you proactively create
# and throw exceptions with custom messages,
# making your code more robust and user-friendly
# when invalid conditions occur.

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age can not be 0")
#     return 10/age


# try:
#     calculate_xfactor(0)
# except ValueError as error:  # error----Class of ValueError
#     print(error)
#     # Using raise to proactively create and throw the exceptions
#     # with coustom message
#     print(type(error))


# 7-Cost of Rasing Exception

# from timeit import timeit

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age can not be 0")
#     return 10/age


# try:
#     calculate_xfactor(0)
# except ValueError as error:
#     pass
# """

# code2 = """
# def calculate_xfactor(age):
#     if age<=0:
#         return None
#     return 10/age


# xfactor = calculate_xfactor(0)
# if xfactor == None:
#     pass
# """
# print("first code=", timeit(code1, number=10000))
# print("second code=", timeit(code2, number=10000))
