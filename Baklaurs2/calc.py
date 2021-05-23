import concurrent.futures as cf
import time as t
import requests as r

def calc():
    with open('Sample2.txt', 'r') as file:
        lines = file.readlines()
        count = 0
        sum = 0
        for line in lines:
            count += 1
            sum += float(line.split(',')[0])
        print((sum / count)*1000)

def calc2():
    for x in range(1, 8):
        with open('selector'+str(x)+'links.txt', 'r') as file:
            sum = 0
            for line in file.readlines():
                sum+=float(line)
            print((sum/100) * 1000)         #Lol tas bija diezgan lieki

def calc3():
    with open('MemoryAsync.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0]
        for x in range(96):
            results[0] += int(lines[x * 5])
            results[1] += int(lines[x * 5 + 1])
            results[2] += int(lines[x * 5 + 2])
            results[3] += int(lines[x * 5 + 3])
            results[4] += int(lines[x * 5 + 4])
        for res in results:
            print(abs(res/100))

def calc4():
    with open('CpuAsync.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0, 0]
        for x in range(96):
            results[0] += float(lines[x * 6].split(",")[1])
            results[1] += float(lines[x * 6 + 1].split(",")[1])
            results[2] += float(lines[x * 6 + 2].split(",")[1])
            results[3] += float(lines[x * 6 + 3].split(",")[1])
            results[4] += float(lines[x * 6 + 4].split(",")[1])
            results[5] += float(lines[x * 6 + 5].split(",")[1])
        for res in results:
            print(abs(res/100))

def calc5():
    with open('Cpus.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0]
        for x in range(100):
            results[0] += float(lines[x * 5])
            results[1] += float(lines[x * 5 + 1])
            results[2] += float(lines[x * 5 + 2])
            results[3] += float(lines[x * 5 + 3])
            results[4] += float(lines[x * 5 + 4])
        for res in results:
            print(abs(res/100))


results = list()

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


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = t.perf_counter()
        func(*args, **kwargs)
        t2 = t.perf_counter()
        results.append([t2 - args[0], t2 - t1, t1 - args[0]])
        return
    return wrapper


@timer
def test_func(t1, url):
    r.get(url)


def test():
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        t1 = t.perf_counter()

        results = [executor.submit(test_func, t1, url) for url in urls]

        for f in cf.as_completed(results):
            yield f.result()


if __name__ == '__main__':
    # calc2()
    # calc()
    calc4()
    # for _ in test():
    #     pass
    # for res in results:
    #     print(res)
