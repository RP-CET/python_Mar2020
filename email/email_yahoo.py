import smtplib
from email.mime.text import MIMEText
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587

sender_yahoo_account ="seow_khee_wei@yahoo.com.sg"
sender_yahoo_password = "your_yahoo_account_passowrd"
sender_email_address ="seow_khee_wei@yahoo.com.sg"
receiver_email_address = "kwseow@gmail.com"
email_msg = "This is a test mail.\n\nRegards"

msg = MIMEText(email_msg)
msg['Subject'] = "Service at appointmentTime"
msg['From'] = sender_email_address
msg['To'] = receiver_email_address

print("Trying to connect o yahoo SMTP server")
smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpObj.set_debuglevel(True)
smtpObj.starttls()

print("Connected.  Logging in...")
smtpObj.login(sender_yahoo_account, sender_yahoo_password)
smtpObj.sendmail(sender_email_address, receiver_email_address, msg.as_string())
smtpObj.quit()

print("Email sent successfully...")
