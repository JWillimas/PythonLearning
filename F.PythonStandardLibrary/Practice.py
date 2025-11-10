# import json 
# from pathlib import Path

#List
# musics=[
#     {"ID":1,"Name":"Thriller","Year":1987},
#     {"ID":2,"Name":"Dangerous","Year":1997}
# ]


# data=json.dumps(musics)#Transfer  musics-List to json Fromat

# Path(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\music.json"
# ).write_text(data)

# text=Path(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\music.json"
# ).read_text()

# print(type(text))

# music_dic=json.loads(text)
# print(music_dic)

#-------------------------------------------------------------------------------------------------------

# import sqlite3
# import json
# from pathlib import Path

# musics=json.loads(Path(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\music.json"
# ).read_text()
# )

# with sqlite3.connect(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\Musics.sqlite3"
# )as conn:
#     command="INSERT INTO Musics Values(?,?,?)"
#     for music in musics:
#             conn.execute(command,tuple(music.values()))
#     conn.commit()

# with sqlite3.connect(
#     r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\Musics.sqlite3"
# )as conn:
#     command="SELECT*FROM Musics"
#     cursor=conn.execute(command)
#     print(cursor.fetchall())

