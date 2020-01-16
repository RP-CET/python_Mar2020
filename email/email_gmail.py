import smtplib
sender_email_address ="kwseow@gmail.com"
sender_email_password = "<your_google_app_password>"
receiver_email_address = "kwseow@gmail.com"
email_title_content = "Subject: Sending Email Using Python\nThis is a test mail."

print("Trying to connect o Gmail SMTP server")
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

print("Connected.  Logging in...")
smtpObj.login(sender_email_address, sender_email_password)

smtpObj.sendmail(sender_email_address, receiver_email_address, email_title_content)
print("Email sent successfully...")

smtpObj.quit()

