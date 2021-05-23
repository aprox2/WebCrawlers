import psutil as psu

memory=[]
on_start = psu.virtual_memory().available

from bs4 import BeautifulSoup
import requests

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


def make_request(url):
    try:
        return requests.get(url, timeout=5)
    except Exception as e:
        e.content = "error"
        return e


def save_res():
    with open('Cpus.txt', 'a') as file:
        for r in all_res:
            file.write(str(r) + "\n")
    with open("Memory.txt", 'a') as file:
        for res in memory:
            file.write(str(res) + "\n")


def get_data(url, i):
    data = make_request(url)
    soup = BeautifulSoup(data.text, "html.parser")
    res = soup.find_all('a', href=True)
    if i % 4 == 0:
        all_res.append(psu.cpu_percent())
        memory.append(str(psu.virtual_memory().available - on_start))


if __name__ == '__main__':
    psu.cpu_percent()
    i=0
    for url in urls:
        i+=1
        get_data(url, i)
    save_res()
    # t1 = time.perf_counter()
    # for url in urls:
    #     get_data(url)
    # t2 = time.perf_counter()
    # print("Total time = ", t2-t1)
    # save_res()