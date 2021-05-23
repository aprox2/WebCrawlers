from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import concurrent.futures as cf
import time

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

def timer(func):
    def wrap(*args, **kwargs):
        t1 = time.perf_counter()
        res, driver = func(*args, **kwargs)
        t2 = time.perf_counter()
        fetchStart = driver.execute_script("return window.performance.timing.fetchStart")
        responseEnd = driver.execute_script("return window.performance.timing.responseEnd")
        elapsed = (responseEnd - fetchStart) / 1000
        driver.quit()
        all_res.append(str(t2-t1-elapsed) + "," + str(elapsed) + "\n")
        return res
    return wrap


@timer
def driver_get(url):
    driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)
    driver.get(url)
    res = driver.page_source
    return res, driver


def handle_requests(urls):
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(driver_get, url) for url in urls]

        for f in cf.as_completed(results):
            yield f.result()


def save_res():
    with open('Sample.txt', 'a') as file:
        for r in all_res:
            file.write(r)




def parse():
    t1_whole = time.perf_counter()
    for response in handle_requests(urls):
        pass
    t2_whole = time.perf_counter()
    print("Total elapsed {}".format(t2_whole - t1_whole))
    save_res()

parse()



def test():
    driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)

    driver.get('https://www.nytimes.com/topic/organization/federal-bureau-of-investigation')

    navigationStart = driver.execute_script("return window.performance.timing.fetchStart")
    responseStart = driver.execute_script("return window.performance.timing.responseEnd")

    backendPerformance = responseStart - navigationStart

    print(backendPerformance)

    driver.quit()
    # elements = driver.find_elements_by_tag_name('a')
    # for element in elements:
    #     href = element.get_attribute('href')
    #     if href is not None:
    #         add_without_dup(href)

# test()

# def add_without_dup(elem):
#     if elem not in urls:
#         urls.append(elem)


# for url in urli:
#     print("PARSING URL : ", url)
#     parse(url)
