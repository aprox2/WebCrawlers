from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import concurrent.futures as cf
import time

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
# for url in urls:
#     print(requests.get(url).elapsed.total_seconds())
#
# exit()


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


def handle_requests(urls):
    with cf.ThreadPoolExecutor(max_workers=100) as executor:
        results = [executor.submit(make_request, url) for url in urls]

        for f in cf.as_completed(results):
            yield f.result()


t1_whole = time.perf_counter()
for x in handle_requests(urls):
    print(x.elapsed.total_seconds())
t2_whole = time.perf_counter()
print("Total elapsed {}".format(t2_whole-t1_whole))


def save_res():
    with open('Sample.txt', 'a') as file:
        for r in all_res:
            file.write(r)


save_res()


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    dom = urlparse(r.url)
    for link in soup.find_all('a', href=True):
        if urlparse(link['href']).netloc:
            add_without_dup(link['href'])
        else:
            add_without_dup(dom.scheme + "://" + dom.netloc + link['href'])


def add_without_dup(elem):
    if elem not in urls:
        urls.append(elem)


if __name__ == '__main__':
    pass
    # handle_requests(urls)
    # r = requests.get('https://en.wikipedia.org/wiki/List_of_Nintendo_Switch_games_(A%E2%80%93F)')
    # # print(r)
    # test = r.elapsed
    # print(test)
    # urls.append('http://quotes.toscrape.com/page/1/')
    # for url in urls:
    #     get_data(url)
    # Spider('https://lv.wikipedia.org/wiki/Vispasaules_t%C4%ABmeklis')


# class Spider:
#
#     def __init__(self, start_url):
#         self.urls = set()
#         self.urls.add(start_url)
#         self.run()
#
#     def run(self):
#         i = 0
#         while self.urls:
#             self.parse(self.urls.pop())
#             i+=1
#             if i > 10:
#                 break
#         for t in self.urls:
#             print(t)
#
#     def parse(self, url):
#         r = requests.get(url)
#         url_info = urlparse(url)
#         soup = BeautifulSoup(r.text, "html.parser")
#         for link in soup.find_all('a', href=True):
#             if urlparse(link['href']).netloc:
#                 self.urls.add(link['href'])
#             else:
#                 self.urls.add(url_info.scheme + "://" + url_info.netloc + link['href'])
#
#
