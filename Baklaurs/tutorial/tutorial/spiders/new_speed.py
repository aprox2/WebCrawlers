import scrapy
import time
import psutil as psu

def save_to_res(results):
    with open('selector7links.txt', 'a') as file:
        for res in results:
            file.write(res + "\n")


class QuotesSpider(scrapy.Spider):
    name = "quotes-speed2"
    # start_urls = [
    #     'http://quotes.toscrape.com/login',
    # ]
    start_urls = [
        'file:///C:/Users/aproxje/PycharmProjects/Baklaurs/tutorial/test7links.html',
    ]
    custom_settings = {
        'CONCURRENT_REQUESTS': 20,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 20                #Lmao es esmu stulbs
    }
    pages = [
        'http://quotes.toscrape.com/tag/world/page/1/',
        'http://quotes.toscrape.com/tag/thinking/page/1/',
        'http://quotes.toscrape.com/tag/yourself/page/1/',
        'http://quotes.toscrape.com/tag/friendship/',
        'http://quotes.toscrape.com/tag/choices/page/1/',
        'http://quotes.toscrape.com/tag/books/',
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/tag/inspirational/',
        'http://quotes.toscrape.com/tag/humor/',
        'http://quotes.toscrape.com/tag/friends/',
        'http://quotes.toscrape.com/tag/contentment/page/1/',
        'http://quotes.toscrape.com/tag/simile/',
        'http://quotes.toscrape.com/tag/obvious/page/1/',
        'http://quotes.toscrape.com/tag/truth/',
        'http://quotes.toscrape.com/tag/misattributed-mark-twain/page/1/',
        'http://quotes.toscrape.com/tag/love/',
        'http://quotes.toscrape.com/tag/love/page/2/',
        'http://quotes.toscrape.com/tag/adventure/page/1/',
        'http://quotes.toscrape.com/tag/reading/'
    ]
    spider_start = time.perf_counter()

    times = 0



    iter = 0

    res_times = []
    memory = []


    init = True

    on_start = psu.virtual_memory().available

    def parse(self, response):
        if self.init:
            self.res_times.append("Vaicajums," + str(psu.cpu_percent()))
            self.init = False
        self.iter += 1
        res = response.css('a::attr(href)').getall()
        if self.iter % 4 == 0:
            self.res_times.append("Dati," + str(psu.cpu_percent(interval=.6)))
            self.memory.append(str(psu.virtual_memory().available - self.on_start))
        for page in self.pages:
            yield scrapy.Request(page, callback=self.parse)
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)

    def close(self, reason):
        with open("Cpus.txt", 'a') as file:
            for res in self.res_times:
                file.write(str(res) + "\n")
        with open("Memory.txt", 'a') as file:
            for res in self.memory:
                file.write(str(res) + "\n")