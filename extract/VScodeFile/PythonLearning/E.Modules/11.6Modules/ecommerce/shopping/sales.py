import sys
import os

# Add the project root to Python path
sys.path.append(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules")
#because vscode can't retrive the location of file 
#So that we need to  add path manipulation at top of sales.py
# Now your imports should work
from ecommerce.customer import contact

print("Sales initialized",__name__)
#__name__:print this module(shopping) name

contact.contact_customer()

# contact.contact_customer()

def calc_shipping():
    pass

if __name__ =="__main__":
    print("Sales started")