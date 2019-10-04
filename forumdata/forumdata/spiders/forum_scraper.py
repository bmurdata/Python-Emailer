import scrapy
import smtplib, ssl
class ForumScraper(scrapy.Spider):
    name="forums"
    fn="../data/url.txt"

    with open(fn,"rt") as f:
         start_urls = [ url.strip() for url in f.readlines()]

    def parse(self, response):
        page = (response.url.split('-')[-1]).split('.html')[0]
        port=465
        smtp_server="smtp.gmail.com"
        senderEmail="YourSener@gmail.com"
        senderpw=input("Enter password")
        message="Subject: {Subject} has Updated!\n\n {Lastpost}\n\nSent by your Friendly Python Emailer. https://github.com/bmurdata/Python-Emailer"
        recieverEmail="YourReiever@gmail.com"

        # filename = 'citydataLastItemEMAIL-%s.txt' % page
    
        filename = 'city-%s.txt' % page
        open(filename) #Guarentee File exists
        filename.close()
        
        with open(filename, 'r+') as f:
            #get some posts, return the last one.
            sellist=response.xpath('//div[@id="posts"]//div[starts-with(@id,"post")]/text()').getall()
            lastpost=sellist[-1]
            fline= f.readline()
            if fline != lastpost:
                print("I found something")
                context=ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
                    server.login(senderEmail,senderpw)
                    message=message.format(Subject="City-Data",Lastpost=lastpost)
                    server.sendmail(senderEmail,recieverEmail,message)
            else:
                print("No new Posts")