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


# ------------------------------
