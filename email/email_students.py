import smtplib, openpyxl
sender_email_address ="kwseow@gmail.com"
sender_email_password = "<your_google_app_password>"
receiver_email_address = "kwseow@gmail.com"

def sendEmail(name, emailId):
    email_body = "Subject: Your attendance. \nDear %s, \nYou were absent for class.\n"%(name)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(sender_email_address, sender_email_password)
    smtpObj.sendmail(sender_email_address, emailId, email_body)
    smtpObj.quit()

workbook = openpyxl.load_workbook("students_attendance.xlsx")
sheet=workbook["Sheet1"]

max_row = sheet.max_row
max_column = sheet.max_column

for i in range(1,max_row+1):
    attendance = sheet.cell(row=i, column=3).value
    if attendance == "Absent":
        name = sheet.cell(row=i,column=1).value
        email = sheet.cell(row=i,column=2).value
        sendEmail(name,email)
        print("Email sent to " + email)
