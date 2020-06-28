import smtplib

client = smtplib.SMTP('localhost',1025)

fromaddr = 'slavko98@gmail.com'
toaddrs = 'slavko98@gmail.com'
msg = 'Hello'

client.sendmail(fromaddr, toaddrs, msg)
client.quit()