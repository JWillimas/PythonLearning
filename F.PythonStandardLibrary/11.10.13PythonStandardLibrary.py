#--------------------------------------------------------------------
#13-Opening the Browser

# import webbrowser

# print("Deployment completed")

# webbrowser.open("http://google.com")
# webbrowser.open("https://www.youtube.com")

#-------------------------------------------------------------------
#14-Sending Emails
#15-Templates:
# In application we use html to build the Templates


# from email.mime.multipart import MIMEMultipart
# #mime :multipurpose internet mail extensions
# #define the format Email message

# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

# import smtplib #Simple Mail Transfer Protocol
# from pathlib import Path
# from string import Template


# template=Template(Path(
#      r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\template.html"
#      ).read_text())


# Directory=[" 17520533671qq@gmail.com"," 1989687823@qq.com"]

# for recipient in Directory:
#     message=MIMEMultipart()
#     message["from"]=" 17520533671qq@gmail.com"
#     message["to"]=recipient
#     message["subject"]="This is a test"

#     body=template.substitute({"name":"John"})

#     message.attach(MIMEText(body,"html"))
#     message.attach(MIMEImage(Path(r"D:\VScodeFile\PythonLearning\F.PythonStandardLibrary\VaultBoy.png").read_bytes()))


#     try:
            
#             with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
#                 smtp.ehlo()#start to communication with server
#                 smtp.starttls()#transter layer security
#                 smtp.login("17520533671qq@gmail.com","alpc leck fddd wyzx")
#                 #I cannot use  regular Gmail password. Need an App Password:
#                 smtp.send_message(message)
#                 print("Sent......")

#     except Exception as e:
#         print(f"❌ Error: {e}")

#--------------------------------------------------------------------
#16-Command-line Argument
# import sys

# print(sys.argv)
#argv:argument varieble

# #In VScode We got to input the whole File Path
# #python "d:\VScodeFile\PythonLearning\F.PythonStandardLibrary\11.10.13PythonStandardLibrary.py" '-a' '-b'


# if len(sys.argv) ==1:#This means user have not supplied any argument
#     #this array always has 1 item(Name of our file)
#     print(f"USAGE: python",
#           "\"d:\\VScodeFile\\PythonLearning\\F.PythonStandardLibrary\\11.10.13PythonStandardLibrary.py\"" ,
#           "<password>")
#     # "\"Escape double Quotes  use '\\'double Quotation to no use the escape char

# else:
#     password=sys.argv[1]
#     print(type(password))
#     print("Password",password)



#--------------------------------------------------------------------

#17-Running External Program
#learn how to run any of the operating system commands
#as well as external programs

import subprocess


completed = subprocess.run(["cmd","/c","false"],
                                                capture_output=True,
                                                text=True,
                                                check=True)#ProcessOpenClass
print("args",completed.args)
print("returncode",completed.returncode)#return any none zero return code stand error
#
print("stderr",completed.stderr)#stand error
print("stdout",completed.stdout)#prefixed with b,binary object












#--------------------------------------------------------------------