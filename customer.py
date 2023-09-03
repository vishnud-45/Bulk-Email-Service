
import pandas as pd
import smtplib as sm
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

sheet_id='1NmsYFVRV94aGIffNAHz8zO8eW7kUq3o1RrtiApQofiA'
df =pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

email_col=df.get("Email")
print(email_col)

user = "duppallivishnu@gmail.com"
password = "heifezsfvlgmqsnm"

try:
    server=sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    from_= user
    to_=email_col

    messege=MIMEText("thank you for registering")
    messege['subject']="welcome"
    messege["from"]="duppallivishnu@gmail.com"
    server.sendmail(from_,to_,messege.as_string())
    print("sent successfully")
   
except Exception as e: 
    print(e)


    