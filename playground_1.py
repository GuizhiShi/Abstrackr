__author__ = 'mq20155490'

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


FROM = "george.shi@mq.edu.au"
TO = ["george.shi@mq.edu.au"]
msg = MIMEMultipart('alternative')
msg['Subject'] = "Hi"
msg['From'] = FROM
msg['To'] ='george.shi@mq.edu.au'
text = MIMEText("IMHERE", 'html')
msg.attach(text)
HOST = 'mail.mq.edu.au'
server = smtplib.SMTP(HOST)
server.sendmail(FROM, TO, msg.as_string())
server.quit()