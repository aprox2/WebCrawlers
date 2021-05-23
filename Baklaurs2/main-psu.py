from bs4 import BeautifulSoup
import requests
import concurrent.futures as cf
import psutil as psu

memory=[]
on_start = psu.virtual_memory().available

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


def handle_requests(urls):
    with cf.ThreadPoolExecutor(max_workers=20) as executor:
        results = [executor.submit(make_request, url) for url in urls]

        for f in cf.as_completed(results):
            yield f.result()


psu.cpu_percent()
i = 0
init = True
for x in handle_requests(urls):
    if init:
        all_res.append("Vaicajums," + str(psu.cpu_percent()))
        init = False
    i+=1
    soup = BeautifulSoup(x.text, "html.parser")
    res = soup.find_all('a', href=True)
    if i % 4 == 0:
        all_res.append("Dati," + str(psu.cpu_percent(interval=.6)))
        memory.append(str(psu.virtual_memory().available - on_start))

def save_res():
    with open('CpuAsync.txt', 'a') as file:
        for r in all_res:
            file.write(str(r) + "\n")
    with open("MemoryAsync.txt", 'a') as file:
        for res in memory:
            file.write(str(res) + "\n")


save_res()



if __name__ == '__main__':
    pass
