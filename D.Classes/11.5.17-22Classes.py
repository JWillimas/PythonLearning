# 17-Good Example of Inheritance

# 18- Abstract Base Classes
# Sub class the parent-class(Stream())
# So that make sure the user get specific using in
# the interface

# purpose to provide some common code to these
# derivitive

# It would be nice to have a common contract
# or common interface across these different typs of string

# 1.derive from abc class
# 2.define the abstrctmethod
# 3.abstract class can't be instanciate
# the class derive from abstract class must define the
# @abstractmethod class method that turn into concrete class


# from abc import ABC,  abstractmethod


# class InvalidationError(Exception):
#     pass


# class Stream(ABC):  # Stream class become abstrct class
#     def __init__(self):
#         self.opend = False

#     # def __str__(self):
#     #     return f"{self.opend}"

#     def open(self):
#         if self.opend:
#             raise InvalidationError("stream is already open")
#         self.opend = True

#     def close(self):
#         if not self.opend:
#             raise InvalidationError("stream is already close")
#         self.opend = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Stream")


# stream01 = NetworkStream()
# stream02 = Stream()
# stream01.open()


# 19-Polymorphism:
# iterate the control
# and call the draw method of each control object
# Polymorphism-ManyForm

# Duck Typing

# from abc import ABC, abstractmethod


# class UIcontrol(ABC):

#     @abstractmethod
#     def draw(self):
#         # only define the contract or interface
#         # all these derivates should follow
#         pass

# class DropDownList:
#     def draw(self):
#         print("Drop down List")


# class TextBox:
#     def draw(self):
#         print("Text Box")


# def draw(controls):
#     for control in controls:
#         control.draw()
#     # Polymorphism behavior
#     # implement the method for multiple time
#     # it only look for the existence of certain methods in ou object


# ddl = DropDownList()
# ddl.draw()
# textbox = TextBox()
# textbox.draw()

# draw([ddl, textbox])


# 21-Extending Built-in
# define a method in child or derivates class

# class Text(str):
#     def duplicate(self):
#         # self represent the current object
#         # which in this case an instance of a string class
#         return self + self


# text = Text("python")
# print(text.upper())

# class Trackbacklist(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)


# list = Trackbacklist()
# list.append("1")
# print(list)


# 22-Data Classes

# If Work with classes that only data and no methods
# you ming wanne to use name tuple instead

# but name tuple we can't mutate them

# from collections import namedtuple

# # Use Point(First-Variable) to store a new creating class
# # Second "Point"-class name
# Point = namedtuple("Point", ["x", "y"])

# print(type(Point))
# P1 = Point(x=1, y=2)
# P2 = Point(x=1, y=2)
# print(P1 == P2)
# FALSE: pythone compare objects base on where they store in memory
