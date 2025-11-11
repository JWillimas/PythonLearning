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





#--------------------------------------------------------------------

#17-Running External Program







#--------------------------------------------------------------------