import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
reciever = 'samira240shifa@gmail.com'
server.login('shinzzzo123@gmail.com', 'hjso bcdl odek hfbm')
server.sendmail('shinzzzo123@gmail.com', reciever, 'hello hello!')

print("mail sent successfully")