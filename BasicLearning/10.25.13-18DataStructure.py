# 13-Stacks
# browsing_session = []
# browsing_session.append()  # add item in browser
# browsing_session.pop()  # pop item out of browser and store it
# browsing_session[-1]  # go to the last Session of browser

# browser_Session = []
# browser_Session.append(1)


# value = browser_Session.pop()
# print(value)


# if not browser_Session:
#     print("error")

# ---------------------------

# 14-Queues
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# value = queue.popleft()
# print(len(queue))

# ---------------------------

# # Memory usage comparison

# from collections import deque
# import sys
# import time

# # Using list as queue
# list_queue = []
# for i in range(10000):
#     list_queue.append(i)
#     if len(list_queue) > 1000:
#         list_queue.pop(0)

#     # Using deque as queue
# deque_queue = deque()
# for i in range(10000):
#     deque_queue.append(i)
#     if len(deque_queue) > 1000:
#         deque_queue.popleft()


# print(f"List memory: {sys.getsizeof(list_queue)} bytes")
# print(f"Deque memory: {sys.getsizeof(deque_queue)} bytes")

# ---------------------------

# 15-Tuples
# Tuple-basicly read only list
# point = tuple("hellow world")
# print(point)

# x, y, *others = point
# print(x)

# ---------------------------

# 16-Swapping Variables
# x = 10
# y = 11

# x, y = (y, x)
# # Using tuple and unpack the tuple in left-side
# # To Swap the Variable in x,y

# print("x", x)
# print("y", y)

# ---------------------------

# 17-Arrays
# Use Arrays only wit dealing with large sequence of numbers
# For perfromence problem

# from array import array
# Data = array("i", [1, 2, 3, 4])
# Data.pop(0)
# print(Data)

# ---------------------------

# 18-Sets
# Set is an unordered collection of unique items
# we cannot have a duplicate
# and this object are unorder they're not in sequence
# so we can not access them using an index

# numbers = [1, 2, 3, 4, 5]

# first = set(numbers)

# second = {1, 5}

# print(first | second)
# # either in the first or in the second set(union)
# print(first & second)
# # (intersection)print the set both in first and sencond set
# print(first - second)
# print(first ^ second)
# # either in the first or second set but not both


# ---------------------------
