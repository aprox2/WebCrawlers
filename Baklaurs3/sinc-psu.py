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


def save_to_res(results):
    with open('Cpus.txt', 'a') as file:
        for res in results:
            file.write(str(res) + "\n")
    with open("Memory.txt", 'a') as file:
        for res in memory:
            file.write(str(res) + "\n")

def parse():
    psu.cpu_percent()
    driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)

    results = []
    i = 0
    for url in urls:
        i += 1
        driver.get(url)
        res = driver.find_elements_by_tag_name('a')
        if i % 4 == 0:
            results.append(psu.cpu_percent())
            memory.append(str(psu.virtual_memory().available - on_start))

    driver.quit()

    save_to_res(results)


if __name__ == '__main__':
    parse()