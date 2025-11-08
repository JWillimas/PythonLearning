# 1-Creating Modules
# # app.py which is main module which is the entry
# # point to our main module

# from sales import calc_shipping, calc_tax

# calc_shipping()
# calc_tax()

# 3-Module Search
# import sales
# import sys  # module

# print(sys.path)
# # sys.path which return the list of directories
# # that python will look at to find a module

# 4-Package
# import ecommerce.sales
# ecommerce.sales.calc_shipping()

#5-dir function

# from ecommerce.shopping import sales
# from ecommerce.customer import contact

# # contact.contact_customer()

# # sales.calc_shipping()

# print(dir(sales))
# #use dir to access all the method and attributes in this object
# print(sales.__name__)
# print(sales.__cached__)
# print(sales.__doc__)

#8-Executing Modules as Script
# import sys
# import os

# # Add the project root to Python path
# sys.path.append(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules")

from  ecommerce.shopping import sales
