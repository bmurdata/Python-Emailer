import scrapy

class ForumScraper(scrapy.Spider):
    name="forums"

    start_urls = [
    'http://www.city-data.com/forum/new-york-city/2156244-staff-analyst-trainee-questions-72.html',
    ]

    def parse(self, response):
        page = response.url..split('-')[-1]

        filename = 'citydata-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.xpath('//'))