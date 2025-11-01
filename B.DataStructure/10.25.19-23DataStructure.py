# 19-dictionary
# # a collection of key value pairs
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)  # The index is name of key
# point["z"] = 20  # add the new key to pairs

# print(point.get("z"))

# del point["x"]  # delet the key in pair
# print(point)

# # Loop-over dictionary

# for key in point:
#     print(key)
# # For loop use in list would Get the element
# # That in dict would Get the key

# for items in point.items():
#     print(items)

# print("\n")

# for (key, value) in point.items():
#     print(key, value)

# ------------------------------

# 20-Dictionary comprehensions
# comprhension:[expression for item in items]

# original code:
# values = []
# for x in range(5):
#     values.append(x*5)

# x-item , range(5)-items(iterable) , x*5-expression

# comprehension code:
# list-
# values = [value*2 for value in range(5)]
# print(values)

# Set-
# values = {value*2 for value in range(5)}
# print(values)

# Dictionary-

# original code:
# values = {}
# for x in range(5):
#     values[x] = x*2
# print(values)

# Comprhension-
# values = {x: x*2 for x in range(5)}
# print(values)

# ------------------------------
# 21-generator expression
# values = (x*2 for x in range(10))
# print(values)
#  this sentence would get generator object

# generator is iterable ,each iteration
# we generate and spit out new value

# values = (x*2 for x in range(1000))
# print(len(values))

# generator don't store the boject in memory
# you won't to get the total number of  items you're working with

# generator got no len ,because we only got the len after
# we iterate over a generator object

# from sys import getsizeof

# values = (x*2 for x in range(10))

# print(getsizeof(values))


# ------------------------------
# 22-Unpacking operator

# take a list into individual elements
# numbers = [1, 2, 3]
# elem, value, *others = numbers
# print(elem, value)
# print(*numbers)  # using asterisk(*)to unpacking the numbers

# values = [*range(5), *"hellow"]
# # unpacking the iterable and store in list values
# print(values)


# Using this to combine two list

# first = [1, 2]
# sec = [3, 4]
# value = [first, "a", sec]
# print(value)  # [[1, 2], 'a', [3, 4]]

# values = [*first, "a", *sec]
# print(values)  # unpacking the elements individually

# Using to unpacking the dictionary

# first = {"x": 1}
# sec = {"x": -1, "y": 1}
# combined = {**first, **sec, "z": 1}  # output:{'x': 10, 'y': 1, 'z': 1}
# # if we have multiply value in the same key
# # the last will be used
# print(combined)

# ------------------------------

# 23-Exercise(find the most repeated char in sentence)

# My_solution:
# sentence = "This is a common interview question"
# char = [*sentence]
# recorder = ''
# Displaydic = {}


# def get_key_from_value(dictionary, value):
#     for key, val in dictionary.items():
#         if val == value:
#             return key
#     return None


# for x in char:
#     counter = 0
#     limit = len(char)
#     y = 0

#     while limit > 0:
#         if x.upper() == char[y].upper():
#             counter += 1

#         y += 1
#         limit -= 1

#     Displaydic[x] = counter

# largest_value = max(Displaydic.values())
# largest_key = get_key_from_value(Displaydic, largest_value)

# print(largest_key)
# print(largest_value)

# ------------------------------

# Mosh_solution:
# from pprint import pprint

# sentence = "This is a common interview question"

# char_frequency = {}

# for char in sentence:  # break the sentence to char individually
#     if char in char_frequency:
#         # ths step directly record the Key&Value to Dict
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1


# # diction is like set, is unorder collection
# # we cannot sort them ,we just can sort list


# # convert dictionary each elements to tuples
# # then store it to a list,list is easy to sort

# char_frenquneces_sorted = sorted(char_frequency.items(),
#                                  key=lambda value: value[1],
#                                  # Using lambda in  tuple
#                                  reverse=True)


# print(char_frenquneces_sorted)
# char_frequency.items(),return all the key value of tuple

# ------------------------------
# # Deep_Seek Solution:

# from pprint import pprint

# sentence = "This is a common interview question"

# char_fre = {}

# for char in sentence:
#     if char in char_fre:
#         char_fre[char] += 1
#     else:
#         char_fre[char] = 1
# # Find max frequency and get all characters with that frequency
# max_freq = max(char_fre.values())
# max_freq_chars = [(char, freq)
#                   for char, freq in char_fre.items() if freq == max_freq]
# # Comprehension:[expression for *unpacking elements in lists(tuple) Filter condition]
# pprint(max_freq_chars)
