# 25.10.16.1 Escape Sequences
# output the special characters you want to print,
# you can use escape sequences.

# \"
# \'
# \\
# \n

# course = 'Python \" programming course\"'
# print(course)

# wrong:course00 = "Python "programming course" "

# course01 = 'Python \' programming course\''
# print(course01)

# course02 = "Python \\ programming course\\"
# print(course02)

# course03 = "Python \n programming course\n"
# print(course03)


# 25.10.16.2 Formatted Strings
# use f before the string to indicate that it is a formatted string.

# first_name = 'John'
# last_name = 'Williams'
# full = first_name+' '+last_name
# print(full)

# full01 = f"{first_name} {last_name}"
# print(full01)

# full02 = f"{first_name.upper()} {2+2+2} {last_name.lower()}"
# print(full02)


# 25.10.16.3 String methon
# every thing in python is an object
# and object have functions
# that functions are called methods

course = '\n Python programming course \n'

# the original string is not affected

# print(course)
# print(course.upper())
# print(course.title())  # capitilize first letter of each word
# print(course.strip())  # remove white space from both side
# print(course.find("O"))  # '-1' mean not found
# print(course.replace("P", "j"))
# print("programming" in course)  # True
# print("programming" not in course)  # False
# print("string" in course)  # False
