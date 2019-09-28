import scrapy

class ForumScraper(scrapy.Spider):
    name="forums"

    start_urls = [
    'http://www.city-data.com/forum/new-york-city/2156244-staff-analyst-trainee-questions-72.html',
    ]

    def parse(self, response):
        page = response.url.split('-')[-1]
        #print(response.xpath('//div[@id="posts"]/text()').get())
        
        filename = 'citydata-%s.html' % page
        with open(filename, 'wb') as f:
            #sellist=response.xpath('//div[@id="posts"]//div[starts-with(@id,"post")]/text()').getall()
            sellist=response.xpath('//div[@id="posts"]//div[starts-with(@id,"post") and position()=(last()-1)]').getall()

            for x in sellist:
                f.write(x.encode())
