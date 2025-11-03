# 1-Classes
# class is a blue print for creating new objects

# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Object:John,Mary Jack

# 2-CreatingClasses
# Pascal Naming Convention

# class Point:
#     def draw(self):
#         print("draw")
# # every point object we creat will have this
# # draw method


# point = Point()
# # inheritance: self-define object
# # call method from  another  object in python
# print(type(point))
# # Output:<class '__main__.Point'>
# # __main__ here is moudle

# print(isinstance(point, Point))
# # if this object is an instance of given class


# 3-Constructors
# The method that we define in a class
# should have at least one parameter
# which by convention is called self
# And this references the current point object we're working with
# when called method of object,should have at least one parameter
# which by convention is called self
# When calling methods in an object We never have to supply
# a value for this parameter.python interpreter does that for us

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         # magic method is called Constructor
#         # and it's executed when we creat a new point object

#     def draw(self):
#         print(f"Point({self.x},{self.y})")
#         # we didn't have to supply a value for the self parameter
#         # Because python does that by default.


# Point.draw(Point(1, 2))
# # If this kind of error appear :
# # missing 1 required positional argument: 'self'
# # We should Add a parameter in to the method

# 4-Class vs Instance Attributes
# Class attribute are share all instances of class
# a class Level attribute share all type

# class Point:
#     defualt_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         # This  atrribute belong to point instance or point object

#     def draw(self):
#         print(f"Point({self.x},{self.y})")


# point = Point(1, 2)
# point.z = 10
# print(point.z)

# Point.draw(point)
# print(point.defualt_color)
# print(Point.defualt_color)


# another = Point(3, 4)
# another.defualt_color = "yellow"
# print(another.defualt_color)
# #PointObject-point , another
# #Attribute-self.x , self.y , defualt_color
# # Manual creat class -Point

# 5-Class vs instance methods
# class Point:
#     defualt_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     # decorate way toextend the behavior of a method
#     def zero(cls):
#         # it's a convention to call this a cls(reference to Point(class))
#         return cls(0, 0)  # define of class

#     def draw(self):
#         print(f"Point({self.x},{self.y})")


# point = Point.zero()  # factory method
# point.draw()

# # def __init__,def draw are instance method
# # def zero is factory method it creat a new object
# # if we want to use a same value repeatly we  can define a
# # factory method

# 6-Magic method(__Str__)
# class Point:
#     defualt_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x},{self.y}) "

#     def draw(self):
#         print(f"Point({self.x},{self.y})")


# point = Point(1.1, 1.1)  # factory method
# print(str(point))


# 7-Comparing Objects
# class Point:
#     defualt_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x},{self.y}) "

#     def __eq__(self, other):    # ==
#         return self.x == other.x and self.y == other.y

#     def __lt__(self, other):
#         return self.x < other.x

#     def draw(self):
#         print(f"Point({self.x},{self.y})")


# point = Point(1, 1)
# other = Point(2, 1)
# print(point < other)

# 8-Arithmetic Operation
