import scrapy
import time
import psutil as psu

def save_to_res(results):
    with open('selector7links.txt', 'a') as file:
        for res in results:
            file.write(res + "\n")


class QuotesSpider(scrapy.Spider):
    name = "quotes-speed"
    # start_urls = [
    #     'http://quotes.toscrape.com/login',
    # ]
    start_urls = [
        'file:///C:/Users/aproxje/PycharmProjects/Baklaurs/tutorial/test7links.html',
    ]
    custom_settings = {
        'CONCURRENT_REQUESTS': 30,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 30                #Lmao es esmu stulbs
    }
    # pages = [
    #     'http://quotes.toscrape.com/tag/world/page/1/',
    #     'http://quotes.toscrape.com/tag/thinking/page/1/',
    #     'http://quotes.toscrape.com/tag/yourself/page/1/',
    #     'http://quotes.toscrape.com/tag/friendship/',
    #     'http://quotes.toscrape.com/tag/choices/page/1/',
    #     'http://quotes.toscrape.com/tag/books/',
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/tag/inspirational/',
    #     'http://quotes.toscrape.com/tag/humor/',
    #     'http://quotes.toscrape.com/tag/friends/',
    #     'http://quotes.toscrape.com/tag/contentment/page/1/',
    #     'http://quotes.toscrape.com/tag/simile/',
    #     'http://quotes.toscrape.com/tag/obvious/page/1/',
    #     'http://quotes.toscrape.com/tag/truth/',
    #     'http://quotes.toscrape.com/tag/misattributed-mark-twain/page/1/',
    #     'http://quotes.toscrape.com/tag/love/',
    #     'http://quotes.toscrape.com/tag/love/page/2/',
    #     'http://quotes.toscrape.com/tag/adventure/page/1/',
    #     'http://quotes.toscrape.com/tag/reading/'
    # ]
    spider_start = time.perf_counter()

    times = 0

    res_times = []

    def parse(self, response):
        results = []
        t1 = time.perf_counter()
        res = response.css('.flag')
        # print(response.xpath('//div[@class = "flag"]'))
        t2 = time.perf_counter()
        results.append(str(t2-t1))
        save_to_res(results)
        return
        t2 = time.perf_counter()
        time_before = response.meta.get('Time-start')
        delay = response.meta.get('download_latency')
        if time_before is not None:
            self.res_times.append({
                "time-start": time_before,
                "time-end": t2,
                "delay": delay
            })
        for page in self.pages:
            t1 = time.perf_counter()
            yield scrapy.Request(page, callback=self.parse, meta={'Time-start': t1})
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)

    def close(self, reason):
        with open("Sample.txt", 'a') as file:
            for res in self.res_times:
                file.write(str(res['time-end'] - res['time-start'] - res['delay']) + "," + str(res['delay']) + "\n")
            file.write("Total time = " + str(time.perf_counter() - self.spider_start) + "\n")