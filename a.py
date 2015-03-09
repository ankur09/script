import smtplib

senders = 'aaa_42kur@yahoo.co.in'
receivers = ['ankursrivastav9958@gmail.com']

message ="""hello ankur this is the new way of sending the message to using python script"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender ,receivers,message)
   print "successfully sent mail"
except SMTPException:
   print "ERROR:unable to send email"
