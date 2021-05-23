import concurrent.futures as cf
import time


def temp(sec, temp):
    print(f'Sleeping for {sec}')
    time.sleep(sec)
    return f'Slept {sec}  {temp}'




test = True


def amazing():
    with cf.ThreadPoolExecutor(max_workers=100) as executor:
        x = [3, 6, 7, 2, 5]
        y = ['a', 'b', 'c', 'd', 'e']
        results = [executor.submit(temp, x, y) for x, y in zip(x, y)]

        for f in cf.as_completed(results):
            yield f.result()


for x in amazing():
    print(x)
