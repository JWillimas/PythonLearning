# 10-FilterFunction
# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 13),
# ]

# x = list(filter(lambda price: price[1] >= 10, items))
# # Using filter function to filt the elements from items list
# # filter object just like map object it's iterable
# # so we can convert to list right away
# y = list(map(lambda item: item[1], x))

# print(y)


# 11-List Comprehension
# More briefly expression of
# Map and filter function

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 13),
# ]

# # take place Map
# # prices = list(map(lambda item: item[1], items))

# prices = [item[1] for item in items]
# # item represents each item in the list(prices)
# # item[1] access the second item of each item(items)
# print(prices)

# # filtered = list(filter(lambda price: price[1] >= 10, items))
# filtered = [item for item in items if item[1] >= 10]
# print(filtered)


# 12-Zip Function
# combining multiple list


# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # print iterable object using list()or for Loop(tuple)
# print(list(zip("abc", list1, list2)))
