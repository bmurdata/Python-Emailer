#Import PyMongo
from pymongo import MongoClient
import scrapy
import emailhelper

class ForumScraper(scrapy.Spider):
    name="citydata"
    #Getting the url.txt file
    fn='url.txt'
    with open(fn,"rt") as f:
         start_urls = [ url.strip() for url in f.readlines()]

    def parse(self, response):
        page = (response.url.split('-')[-1]).split('.html')[0]
        filename = 'city-%s.txt' % page
        
        with open(filename, 'r+') as f:
            #get some posts, return the last one.
            sellist=response.xpath('//div[@id="posts"]//div[starts-with(@id,"post")]/text()').getall()
            lastpost=sellist[-1]
            fline= f.readline()
            if fline != lastpost:
                f.write(lastpost)
                print("I found something")
                emailhelper.emailSend(emailhelper.message,page,lastpost)
            else:
                print("No new Posts")

#Uses Docker Toolbox for Windows, with a VirtualBox URL of the below.
client= MongoClient('192.168.99.100',27017)
#Define the database and Collection to be used by the program.
db= client.testtwo
testscr=db.testcol2
test= {"url":"http://www.city-data.com/forum/new-york-city/2156244-staff-analyst-trainee-questions-72.html",
        "lpost":"LAGGY"}

testscr.insert_one(test)
print(testscr.find_one({"lpost":"LAGGY"}))

# docker exec -it mantau bash
# docker run -d -it --name mantau -p 27017:27017 mongo