import smtplib 
import ssl 
from email.message import EmailMessage

subject ="Email From Python"
body ="Testing body from python"
sender_email = "tahsindemo@gmail.com"

receiver_email = "tahsinahmed52225@gmail.com"
password = input("Enter your password:")


message = EmailMessage()
message['From']=sender_email
message['To']=receiver_email
message['Subject']=subject
#Adding the content body to mail


print("Sending Email...")
with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
    server.ehlo()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())
    server.close()
print("Success")
