import scrapy
import smtplib, ssl
import os

class ForumScraper(scrapy.Spider):
    name="forums"
    #Searches two directories up from location of forum_scraper
    #Getting the url.txt file
    fileTest='..\\..\\data\\url.txt'
    fn = os.path.join(os.path.dirname(__file__), fileTest)

    

    with open(fn,"rt") as f:
         start_urls = [ url.strip() for url in f.readlines()]

    def parse(self, response):
        #Gets the -72 Page number from the link:
        #http://www.city-data.com/forum/new-york-city/2156244-staff-analyst-trainee-questions-72.html

        page = (response.url.split('-')[-1]).split('.html')[0]
        #Used in SSL email sending, defining sender email, pw, and 
        #reciever emails.
        port=465
        smtp_server="smtp.gmail.com"
        senderEmail=input("Enter Gmail Email(without @gmail.com): ")+"@gmail.com"
        print(senderEmail)
        senderpw=input("Enter password: ")
        message="Subject: {Subject} has Updated!\n\n New post below:\n\n{Lastpost}\n\n"+"Sent by your Friendly Python Emailer. https://github.com/bmurdata/Python-Emailer"
        recieverEmail=input("Enter reciving Gmail Email(without @gmail.com): ")+"@gmail.com"    
        filename = 'city-%s.txt' % page
        #Creates and closes file where the mos recent post will be stored, if it doesn't exist
        open(filename,'a').close()
        #Ask user if they want to clear file for testing purposes.
        choice=input("Do you want to clear the file where the lastpost is store?(Y/N): ")
        if choice=="Y":
            open(filename, 'w').close()
        
        with open(filename, 'r+') as f:
            #get some posts, return the last one.
            sellist=response.xpath('//div[@id="posts"]//div[starts-with(@id,"post")]/text()').getall()
            lastpost=sellist[-1]
            fline= f.readline()
            if fline != lastpost:
                f.write(lastpost)
                print("I found something")
                #Login to email and send a response.
                context=ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
                    server.login(senderEmail,senderpw)
                    message=message.format(Subject="City-Data Page "+page,Lastpost=lastpost)
                    server.sendmail(senderEmail,recieverEmail,message)
            else:
                print("No new Posts")