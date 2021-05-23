from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import concurrent.futures as cf
import time

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

def timer(func):
    def wrap(*args, **kwargs):
        t1 = time.perf_counter()
        res, driver = func(*args, **kwargs)
        t2 = time.perf_counter()
        fetchStart = driver.execute_script("return window.performance.timing.fetchStart")
        responseEnd = driver.execute_script("return window.performance.timing.responseEnd")
        elapsed = (responseEnd - fetchStart) / 1000
        all_res.append(str(t2-t1-elapsed) + "," + str(elapsed) + "\n")
        return res
    return wrap


@timer
def driver_get(driver, url):
    driver.get(url)
    res = driver.page_source
    return res, driver


def save_res():
    with open('Sample3.txt', 'a') as file:
        for r in all_res:
            file.write(r)


def get_file(file):
    with open(file, 'r') as file:
        return file.read()

def save_to_res(results):
    with open('selector7links.txt', 'a') as file:
        for res in results:
            file.write(res + "\n")

def parse():
    # driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)
    data = get_file('test7links.html')
    # driver.get("data:text/html;charset=utf-8," + data)
    results = []
    #Pajautāt vajag
    for z in range(100):
        print(z)
        driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)
        driver.get("data:text/html;charset=utf-8," + data)
        t1 = time.perf_counter()
        res = driver.find_elements_by_tag_name('a')
        # res = driver.find_element_by_class_name("flag")
        t2 = time.perf_counter()
        results.append(str(t2-t1))
        driver.quit()
    save_to_res(results)
    print("Time spent = ", t2-t1)
    return
    t1 = time.perf_counter()
    for url in urls:
        driver_get(driver, url)
    t2 = time.perf_counter()
    print("Time elapsed : ", t2-t1)
    save_res()


if __name__ == '__main__':
    parse()