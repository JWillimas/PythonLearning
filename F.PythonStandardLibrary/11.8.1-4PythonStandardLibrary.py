#2-Work with Path
# import sys
# import os

# sys.path.append(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules")

# from pathlib import Path

# path=Path(r"my_creating_path\not_yours")
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path=path.with_name(".txt")
# #creat a new path object based on this existing path
# #but only change the name and the extension of file
# print(path)
# print(path.suffix)
# print(path.absolute())

#--------------------------------------------------------------------


#3-Work with Directories
# from pprint import pprint

# import sys
# import os

# sys.path.append(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules\ecommerce")


# from pathlib import Path
# path=Path(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules\ecommerce")
# #if crrent working directory is different from where "ecommmerce" folder is located
# #Use Absoluted Path

# paths=[p for p in path.iterdir() ]

# #iterdir() has two limitations 
# #one is we cannot search by the patterns 
# #second is it doesn't search recursively

# py_files=[p for p in path.glob(r"**\*.py")]

# #Use ("**/*.py") to search cursviely

# all_py_files=[p for p in path.rglob("*.py")]


# pprint(py_files)

# print('\n')

# pprint(all_py_files)

#--------------------------------------------------------------------


#4-Working with File
#Operate the file by code

# from pathlib import Path
# from time import ctime


# path=Path(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules\ecommerce\__init__.py")

#path.exists()
#path.unlink()

# print(ctime(path.stat(). st_birthtime))

# with open(path,"r") as file:
#     content=file.read()
# print(content)

# print(path.read_text())

#path.write_text()


#copy certain file to appointed location
#Classic Way
# source=Path(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules\ecommerce\__init__.py")
# target=Path(r"d:\VScodeFile\PythonLearning\F.PythonStandardLibrary")/"__init__.py"

# target.write_text(source.read_text())

# #Shell-utilities Way
# import shutil
# shutil.copy(source,target)










