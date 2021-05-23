from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import concurrent.futures as cf
import time
import psutil as psu


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
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        all_res.append(str(t2-t1-res.elapsed.total_seconds()) + "," + str(res.elapsed.total_seconds()) + "\n")
        return res
    return wrap


@timer
def make_request(url):
    try:
        return requests.get(url, timeout=5)
    except Exception as e:
        e.content = "error"
        return e


def save_res():
    with open('Sample2.txt', 'a') as file:
        for r in all_res:
            file.write(r)


def get_file(file):
    with open(file, 'r') as file:
        return file.read()

def save_to_res(results):
    with open('selector2links.txt', 'a') as file:
        for res in results:
            file.write(res + "\n")

def get_data():
    data = get_file('test2links.html')
    soup = BeautifulSoup(data, "html.parser") #For testing selectors
    results = []
    for _ in range(100):
        t1 = time.perf_counter()
        res = soup.find_all('a', href=True)
        # res = soup.find_all('a', href=True)
        t2 = time.perf_counter()
        results.append(str(t2 - t1))
    save_to_res(results)

    # soup = BeautifulSoup(r.text, "html.parser")
    # dom = urlparse(r.url)
    # for link in soup.find_all('a', href=True):
    #     if urlparse(link['href']).netloc:
    #         add_without_dup(link['href'])
    #     else:
    #         add_without_dup(dom.scheme + "://" + dom.netloc + link['href'])


def add_without_dup(elem):
    if elem not in urls:
        urls.append(elem)


if __name__ == '__main__':
    get_data()
    # t1 = time.perf_counter()
    # for url in urls:
    #     get_data(url)
    # t2 = time.perf_counter()
    # print("Total time = ", t2-t1)
    # save_res()