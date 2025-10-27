# 1-list
# list can store num,letter,Matrix...
# Letter = ["a", "b", "c"]
# print(f"{Letter}\n")

# Matrix = [[1, 2], [2, 3], [3, 4]]
# print(f"{Matrix}\n")

# Zeros = [0]*5
# print(f"{Zeros}\n")

# Combined = Zeros+Matrix
# print(f"{Combined}\n")

# # Using of rang and list function
# # Rang is iterable
# Number = list(range(1, 20))
# # range is start defaults to 10 ,and stop is omitted
# print(f"{Number}\n")

# char = list("hellow world")
# print(f"{char}\n")
# print(len(char))


# 2-Accessing Items
# letters = list("abcd")
# Letters = ["A", "B", "C", "D"]

# Numbers = list(range(20))


# letters[0] = "A"

# print(Numbers[::-1])
# this will return all the items in the original list
# but in reverse order.

# 3-Unpacking Lists

# numbers = [1, 2, 3, 4, 4, 4]
# fir, sec, *others = numbers
# unpacking-unpack the numbers to the
# left side of silent operator,use asterisk there
# packing all the other items into a seperate list
# like :def multiply(*items)
#               items(1,2,3,4)

# items<<-----unpack<<----list

# 4-Loop Over List
# numbers = list(range(20))
# for i in range(10):
#     print(numbers[i])
# letters = list("abc")
# for i in letters:  # use for loop to loop over this list
#     print(i)

# letters = list("abc")
# for i in enumerate(letters):
#     # enumerate:give a index to letters's list
#     print(i[0], i[1])
# # in the loop ,use "[]"the letters will unpack-->>to the i
# print("\n")

# for index, letter in enumerate(letters):
#     print(index, letter)
# in this Loop,use "[]"the letters will unpack-->>to the index&letter

# 5-Add or Remove items
# If we want to replace items in list:
# items = [0, 1, 2]
# items[0] = 1
# print(items)

# Add:
# letters = list("ssbbbbbfrfbbbb")
# numbers = list("122233444")

# letters.append("d")  # add a object in the end of the list
# letters.insert(1, "-")  # insert a object before the list
# print(letters)

# print(letters)
# print("\n")

# print(numbers)
# print("\n")


# letters.insert(0, "0")

# Remove

# letters.pop(0)  # pop()-->>delet a num from the assign index
# letters.remove("b")#Rmove(char)-->>remove a items from list
# del letters[0:3]#Remove[0:3]-->>remove a range of index items from list
# letters.clear()#-->>clear the items in the list

# while "b" in letters:
#     letters.remove("b")
#     print(letters)

# letters = [i for i in letters if i != 'b']  # letters=[i] and iteration in list
# print(letters)

# print("\n")
# numbers = [int for int in numbers if int != '3']
# print(numbers)

# 6-Finding Items
# Letters = list("abcddddd")
# indices = [i for i, char in enumerate(Letters) if char == 'd']
# print(indices)

# indices=[i......]the expression to include new items in the new list

# Letters.index(),tell the char's index in the list

# print(Letters.count("d"))
# Letters.count("items") the numbers of occurrences of given items
