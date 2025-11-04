# 9-Creating Custom Containers
# It supports various operators around container

# 10-Using "__"to prevent access private members
# F2-choice and modify all the chosen variable

# class TagCloud:
#     # get python classes to act like built in sequence-->container
#     def __init__(self):
#         self.__tags = {}  # double underscore set it private
#         # Define the TagCloud as a dict

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

# because of the __getitem__ whe can get the value of cloud[Key]

#     def __setitem__(self, tag, value):
#         self.__tags[tag.lower()] = value

#     def __iter__(self):
#         iter(self.__tags)

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1


# cloud = TagCloud()
# cloud.add("python")
# print(cloud.__tags)


# print(cloud.__dict__)  # get the key of class dict
# print(cloud._TagCloud__tags)  # using this to get the private value

# 11-Properties:

# Properties is an object sit in front of an attribute
# and allows us to get or set the value of attribute

# Using the method would polluting the interface of our object
# We want our object or function expose less to outside


# @classmethod using decorator
# to convert an instance method to class method

# Instance method work with object data, class methods
# work with class-level data and are often uesd for alternative
# constructors or class-wide operations

# class Product:
#     def __init__(self, price):
#         self.__value = price

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, price):
#         if price < 0:
#             raise ValueError("price can't be negative")
#         self.__value = price

# price = Product(10)
# price.value = 100
# price.value = -100
# print(price.value)

# 12-inheritance
# a mechanism wtaht allows us to define the
# common behavior or common functions in one class
# and then inheritence to other class

# 13-The Object Class

# 14-method override
# replacing or extending a method defined
# in the basic class.

# class Animal(object):  # default inheritange from object
#     def __init__(self):
#         self.age = 1
#         # animal class has self.age constructor where
#         # initalize the age attribute to 1

#     def eat(self):
#         print("eat")


# class mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         self.age = 2

#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def __init__(self):
#         self.age = 3
#         super().__init__()
#         # super():Using the last __init__ attribute

#     def swim(self):
#         print("swim")


# fish = mammal()
# print(fish.age)

# 15-
