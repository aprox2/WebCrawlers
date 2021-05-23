from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import concurrent.futures as cf
import time
import psutil as psu

memory=[]
on_start = psu.virtual_memory().available

chrome_options = Options()
chrome_options.add_argument("--headless")

drivers = list()

urls = [
        'http://quotes.toscrape.com/login',
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
all_res = []


def driver_get(driver, url, i):
    driver.get(url)
    res = driver.find_elements_by_tag_name('a')
    drivers.append(driver)
    return res


def handle_requests(urls):
    results = []
    with cf.ThreadPoolExecutor(max_workers=driver_count) as executor:
        for url, i in zip(urls, range(1, 21)):
            if not drivers:
                while True:
                    if drivers:
                        break
            results.append(executor.submit(driver_get, drivers.pop(), url, i))
        for f in cf.as_completed(results):
            yield f.result()


def save_res():
    with open('CpuAsync4.txt', 'a') as file:
        for r in all_res:
            file.write(str(r) + "\n")
    with open("Memory3.txt", 'a') as file:
        for res in memory:
            file.write(str(res) + "\n")




driver_count = 20

def parse():
    for _ in range(driver_count):
        drivers.append(webdriver.Chrome('driver/chromedriver.exe', options=chrome_options))
    psu.cpu_percent()
    i = 0
    init = True
    for response in handle_requests(urls):
        if init:
            all_res.append("Vaicajums," + str(psu.cpu_percent()))
            init = False
        i += 1
        if i % 4 == 0:
            all_res.append("Dati," + str(psu.cpu_percent(interval=.6)))
            memory.append(str(psu.virtual_memory().available - on_start))

    for drive in drivers:
        drive.quit()

    save_res()

parse()


