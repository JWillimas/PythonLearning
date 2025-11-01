# 7-Sorting list
# numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)  # sort is sort the original list
# print(sorted(numbers))  # sorted is return a new list
# print(numbers)

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 13),
# ]  # (product1,10) is a tuple(the structure of data that has several part)


# def sort_item(i):
#     return i[1]


# items.sort(key=sort_item)
# print(items)

# items = [
#     (7, 1),
#     (6, 1),
#     (5, 1),
#     (4, 1),
#     (3, 1),
# ]


# def item_arrange(item):  # parameters
#     return item[0]  # return the index0 as result


# items.sort(key=item_arrange)
# #   Using sort method ,the items list as argument
# #   for key function
# print(items)

# 8-Lambda Function
# Improve the sort code and make it clearer by use Lambda
# The lambda function syntax:
# lambda item : item[1]
# item para represent each item in the list
# item[1] accesses the second element of each item

# items = [
#     (7, 1),
#     (6, 1),
#     (5, 1),
#     (4, 1),
#     (3, 1),
# ]

# items.sort(key=lambda item: item[0])
# # use the elements of the index as the sort key

# print(items)

# 9-Map function
# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 13),
# ]
# # prices = []
# # for item in items:
# #     # item will receivel each tuple in items in this Loop
# #     prices.append(item[1])
# #     # add the index element in to the end of the list
# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)


# Self-practice :input a series of product name and price
# then store it and sort it in ascending order

# products = []

# while True:
#     print("\n(input 'F' finish)\n(input 'P' to print the Bill)")

#     product = input("please input your product :\n")

#     if product.upper() == 'F':
#         break

#     if product.upper() == 'P':

#         products.sort(key=lambda property: property[1])
#         for Row in products:
#             print(f"\n[{Row}]")
#         print("-------------------------------------")

#     if product.upper() != 'P':

#         print("\n(input 'F' finish)\n(input 'P' to print the Bill)")

#         price = input("please input your price:\n")

#         if price.upper() == 'F':
#             break
#         if price.upper() == 'P':
#             products.sort(key=lambda property: property[1])
#             for Row in products:
#                 print(f"\n[{Row}]")
#             print("-------------------------------------")

#         if price.upper() != 'P':
#             products.append((product, int(price)))
