# 1-Comparations
# if (10 > 3)?
# if "bag">"BAG"?


# 2-Conditional Statements

temp = input("temp =")
temp = int(temp)
# if temp > 22:
#     print("sweating!!!")
# elif temp > 20:
#     print("nice weather")
# else:
#     print("cold!!!")

# ternary operator
message = "Sweating!!!"if temp > 22 else "Nice weather" if temp > 20 else "cold!!!"
print(message)
