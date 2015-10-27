import ftplib

session = ftplib.FTP('52.3.120.23','ftpuser','ftpuser')
file = open('20150909-183923.jpg','rb')                  # file to send
try:
	session.storbinary('STOR 20150909-183923.jpg', file)     # send the file
except:
	pass
	
file.close()                                    # close file and FTP
session.quit()
