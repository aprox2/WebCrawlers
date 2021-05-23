def calc():
    with open('Sample3.txt', 'r') as file:
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
    with open('Cpus.txt', 'r') as file:
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
    with open('CpuAsync4.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0, 0]
        for x in range(51):
            results[0] += float(lines[x * 6].split(",")[1])
            results[1] += float(lines[x * 6 + 1].split(",")[1])
            results[2] += float(lines[x * 6 + 2].split(",")[1])
            results[3] += float(lines[x * 6 + 3].split(",")[1])
            results[4] += float(lines[x * 6 + 4].split(",")[1])
            results[5] += float(lines[x * 6 + 5].split(",")[1])
        for res in results:
            print(abs(res/51))

def calc5():
    with open('Memory3.txt', 'r') as file:
        lines = file.readlines()
        results = [0, 0, 0, 0, 0]
        for x in range(51):
            results[0] += float(lines[x * 5])
            results[1] += float(lines[x * 5 + 1])
            results[2] += float(lines[x * 5 + 2])
            results[3] += float(lines[x * 5 + 3])
            results[4] += float(lines[x * 5 + 4])
        for res in results:
            print(abs(res/51))


if __name__ == '__main__':
    # calc()
    calc4()