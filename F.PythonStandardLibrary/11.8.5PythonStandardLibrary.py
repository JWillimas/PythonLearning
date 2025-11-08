#5-Working with Zip Files:
# from pathlib import Path
# from zipfile import ZipFile
# from pprint import pprint

# path=Path(r"d:\VScodeFile\PythonLearning\E.Modules\11.6Modules")

#Get all the file from ecommerce directory and Write it to Zip File

# try:
#     zip=ZipFile("file.zip","w")
#     for file in path.rglob("*.*"):
#         zip.write(file)

# finally:
#     zip.close()

#if there is some chance something gose wrong here
#use try ...finally to excecute it 
#if not zip.close() after iterable program maybe corrupt

# with  ZipFile("file01.zip","w") as zip:
#     for file in path.rglob("*.*"):
#         zip.write(file)

# #use with....as method the Zip file is automatically closed and finalized here

    
# with ZipFile("file01.zip") as zip:
#     #pprint(zip.namelist())

#     info=zip.getinfo('VScodeFile/PythonLearning/E.Modules/11.6Modules/ecommerce/shopping/sales.py')
    
#     print(info)
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")
    
    
    #get the all file name from zip


#--------------------------------------------------------------------
#6-Working with CSV(Common Seperate Value) Files












#--------------------------------------------------------------------
