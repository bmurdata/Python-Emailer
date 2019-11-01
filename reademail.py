#import emailhelper
import smtplib, ssl
import email
import imaplib
import base64
import re
from pymongo import MongoClient
#Uses Docker Toolbox for Windows, with a VirtualBox URL of the below.
client= MongoClient('192.168.99.100',27017)
#Define the database and Collection to be used by the program.
db= client.pyemailer
dbcol=db.linklist

#SMTP and Email reply logic
port=465
smtp_server="smtp.gmail.com"
#Messages if the Link is in the Database or not.
message="Subject: {Subject} has been added!\n\n New link:\n\n{Lastpost}\n\n"+"Sent by your Friendly Python Emailer. https://github.com/bmurdata/Python-Emailer"
message2="Subject: {Subject} already exists!\n\n Verify:\n\n{Lastpost}\n\n"+"Sent by your Friendly Python Emailer. https://github.com/bmurdata/Python-Emailer"

context=ssl.create_default_context()

senderEmail=input("Enter Gmail Email(without @gmail.com): ")+"@gmail.com"
senderpw=input("Enter password: ")
recieverEmail=input("Enter reciving Gmail Email(without @gmail.com): ")+"@gmail.com"
def emailSend(message,page,lastpost):
    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
                    server.login(senderEmail,senderpw)
                    message=message.format(Subject="City-Data Page "+page,Lastpost=lastpost)
                    server.sendmail(senderEmail,recieverEmail,message)
#Regular expressions to search for in the email.
cdre="http://www.city-data.com/forum/new-york-city/2156244-staff-analyst-trainee-questions-(\d+).html"

#email checking test
mail = imaplib.IMAP4_SSL('imap.gmail.com')
femail=senderEmail
fpw=senderpw

mail.login(femail,fpw)
mail.select('inbox')
efilter='(FROM "'+recieverEmail +'")'
resp,items=mail.search(None,efilter)
items=items[0].split() #get mail ids
# items[::-1]
for emailid in items:
    typ, data=mail.fetch(emailid,"(RFC822)")#   ""  (RFC822)  (UID BODY[TEXT])
    #print(data[0][1])
    raw_email=email.message_from_bytes(data[0][1])
    if raw_email.is_multipart():
        #payload is the message of the email. I think. Which is then decoded from base64 into utf-8
        payload=raw_email.get_payload()[0]
        emailbody=base64.b64decode(payload.get_payload()).decode("utf-8")
        #print(emailbody)
        msrch=re.search(cdre,emailbody)
        if(msrch):
            print("Found a link!")
            #print(msrch.group())
            
            if(dbcol.find_one({'url':msrch.group()})):
                emailSend(message2,msrch.group(),msrch.group())
                print("Link found but already in DB.")
            else:
                dbcol.insert_one({'url':msrch.group()})
                emailSend(message,msrch.group(),msrch.group())
                print("New link found, and email sent")
                

        else:
            print("No New Links found in the email. Womp."+str(emailid))
    else:
        print("Not multipart")
        print(base64.b64decode(raw_email.get_payload()))

mail.close()
mail.logout()