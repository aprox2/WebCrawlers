import scrapy
import time


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        next_page = response.css('a::attr(href)').getall()
        if not next_page:   #Parbauda vai saraksts nav tukšs
            return
        for page in next_page:
            page = response.urljoin(page)
            t1 = time.perf_counter()
            yield scrapy.Request(page, callback=self.parse)
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
