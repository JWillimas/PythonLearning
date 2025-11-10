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
# import csv

# with open(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\data.csv","w",
#     newline="") as file:
#         writer=csv.writer(file)
#         writer.writerow(["transaction_id","product_id","price_id"])
#         writer.writerow([1000,10,5])
#         writer.writerow([100,3,15])

# #Rewrite the content from dsv by modify the argument in writerow

# with open(
#         r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\data.csv") as file:
        
#         # Reader=list(csv.reader(file))
#         # #Reader is iterable
#         # print(Reader)
#         # #The index got to end when finish the print

#         for read in csv.reader(file):
#                 print(read)

#--------------------------------------------------------------------

#7-Working with JSON(JavaScript Object Notation) Files

# import json
# from pathlib import Path
 
# movies= [
#     {"id":1,"little":"Terminator","year":1989},
#     {"id":2,"little":"kindergardeten Cop","year":1993}
# ]

# data= json.dumps(movies)
# Path(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\movies.json").write_text(data)

# text=Path(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\movies.json").read_text()

# print(type(text))

# movies=json.loads(text)
# print(movies[0])
# print(type(movies))

#--------------------------------------------------------------------

#8-Working with a SQLite(Structured Query Language) Database

#read all the movie form json script and store to the SQLite Database

#connection object similar to file should be close when you're done

# import sqlite3
# import json
# from pathlib import Path


#Write Data from database:
# movies=json.loads(Path(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\movies.json").read_text())

# with sqlite3.connect(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\db.sqlite3")as conn:
#     command ="INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#             conn.execute(command,tuple(movie.values()))        
#     conn.commit()



#Read Data from database:

# with sqlite3.connect(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\music.sqlite3"
# )as conn:
#    command="SELECT * FROM Movies"
#    cursor=conn.execute(command)
#    for row in cursor:
#       print(row)

#--------------------------------------------------------------------
#9-Working with TimeStamps

#Use to calculate excecute time for some piece of code

# import time

# def SendMessage():
#     for i in range(10000):
#         pass

# start=time.time()
# SendMessage()
# End=time.time()
# dur=End-start
# print(dur)

#--------------------------------------------------------------------
#10-Working with Data Times
# from datetime import datetime
# import time

# dt1=datetime(2018,1,1)
# dt2=datetime.now()
# dt3=datetime.strptime("2019/1/1","%Y/%m/%d")
# dt4=datetime.fromtimestamp(time.time())


# print(dt1)
# print(dt2)
# print(dt3)
# print(dt4)

#--------------------------------------------------------------------
#11-Working with Time Deltas










#--------------------------------------------------------------------