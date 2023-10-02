import datetime
import yagmail
import os 
today = datetime.date.today()
file = "teesheet-"+str(today)+".pdf"
FILE_DIRECTORY  = "REPLACE VALUES"
SEND_EMAIL = 'REPLACE VALUES'
EMAIL_PASS = 'REPLACE VALUES'
RECEIVE_EMAIL = 'REPLACE VALUES'
OAUTH_FILE = "REPLACE VALUES"


yag = yagmail.SMTP(SENDER_EMAIL,PASSWORD, oauth2_file=OAUTH2_FILE)
yag.send(RECEIVER_EMAIL,'subject',attachments=[FILE_DIRECTORY+file])

path = os.path.join(FILE_DIRECTORY, file)                                                                       
os.remove(path)
