for n in range(4, 100):
    s = '3' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s: s = s.replace('25', '3', 1)
        if '355' in s: s = s.replace('355', '52', 1)
        if '555' in s: s = s.replace('555', '23', 1)
    if sum(map(int, s)) == 27:
        print(n)
        break

# хз правильно или нет , полного квадрата количесвто найти за счет суммы s
k = 0
for n in range(3,1000):
    s = '3' + '2' * n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    for i in range(1,1000):
        if sum(map(int, s)) == i * i:
            k += 1
            print(k)


for x in range(50):
    for y in range(50):
        for z in range(100):
            s = '0' + x * '1' + y * '2' + z * '3'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 50 and s.count('2') == 12 and s.count('3') == 7:
                print(x)
                break
