#---------------------------------------
#1-install Request
#put it in shell:
#python -m pip install requests


#---------------------------------------
#2-Virtual Enviorment
#Promble :we have another project in rhat project 
#we only use the earlier version of the package

#put it in shell:
#python -m pip install virtualenv

#Create a Virtual enviorment
#:cd D:\VScodeFile\PythonLearning
#python -m venv venv

#And go to 
# D:\VScodeFile\PythonLearning\G.Packagning\G.PackageIndex\.venv\Scripts\Activate.ps1
#to anctivite the venv
import requests
print(requests.get("http://google.com"))

#---------------------------------------
#5-Virtual Enviorment in VScode

#---------------------------------------
#6-PIpFile :
#Chances are in the future 
# when we put this project on a different machine
#And install denpendencies 
# we might have a newer version of request package

#install pipenv:pip install pipenv
#install requests : pipenv install requests 
#--------------------------------------- 



