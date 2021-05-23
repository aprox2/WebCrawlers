import concurrent.futures as cf
import time as t
import os
from sys import argv
import psutil as psu
import math as m
import hashlib

NAME = argv[0]

def calc():
    with open('Sample.txt', 'r') as file:
        lines = file.readlines()
        count = 0
        sum = 0
        for line in lines:
            count += 1
            sum += float(line.split(',')[0])
        print((sum / count)*1000)

def new_calc():
    x = [1.8156 ,1.9132, 1.8525]
    sum = 0
    for elem in x:
        sum += elem
    print(sum/3)

def calc2():
    for x in range(1, 8):
        with open('selector'+str(x)+'links.txt', 'r') as file:
            sum = 0
            for line in file.readlines():
                sum+=float(line)
            print((sum/100) * 1000)         #Lol tas bija diezgan lieki

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

def test():
    return {
        "CPU in use": psu.cpu_percent(interval=1),
        "Memory in use": psu.virtual_memory().used,
    }
    # for proc in psu.process_iter(attrs=("cmdline", "name", "cpu_percent", "memory_percent")):
        # cmd = proc.info["cmdline"]
        # if "python" in proc.info["name"] and cmd is not None and len(cmd) > 0 and NAME in cmd[-1]:
        #     return {
        #         "CPU in use": proc.cpu_percent(interval=1),
        #         "Memory in use": proc.info['memory_percent'],
        #         "Memory usage": psu.virtual_memory().total*(proc.info["memory_percent"]/100)/(1024**3)
        #     }

def calc3():
    with open('Memory.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0]
        for x in range(100):
            results[0] += int(lines[x * 5])
            results[1] += int(lines[x * 5 + 1])
            results[2] += int(lines[x * 5 + 2])
            results[3] += int(lines[x * 5 + 3])
            results[4] += int(lines[x * 5 + 4])
        for res in results:
            print(abs(res/100))

def calc4():
    with open('Cpus.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0, 0]
        for x in range(100):
            results[0] += float(lines[x * 6].split(",")[1])
            results[1] += float(lines[x * 6 + 1].split(",")[1])
            results[2] += float(lines[x * 6 + 2].split(",")[1])
            results[3] += float(lines[x * 6 + 3].split(",")[1])
            results[4] += float(lines[x * 6 + 4].split(",")[1])
            results[5] += float(lines[x * 6 + 5].split(",")[1])
        for res in results:
            print(abs(res/100))

if __name__ == '__main__':
    # calc()
    # new_calc()
    # calc2()
    calc4()
    # os.system('cmd /c "scrapy crawl quotes-speed"')
