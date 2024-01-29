f = open('26-111.txt')

K = int(f.readline())                              #багажи (досрок 2023
N = int(f.readline())

a = []

for i in range(N):
    st, end = map(int, f.readline().split())
    a.append([st, end])
a.sort()
#время окончания хранения багажа в ячейках
camera = [0] * K
count = 0
last = 0
for i in range(N):
    st, end = a[i]
    for j in range(K):
        if camera[j] < st:
            camera[j] = end
            count += 1
            last = j+1
            break
print(count, last)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
f = open('26-111.txt')

M , N = map(int, f.readline().split())

a = []

for i in range(N):
    st , r = map(int, f.readline().split())
    a.append([st, st + r, r])

a.sort(key = lambda x: x[0])

bank = [0] * M
bankc = [0] * M
last = 0
for i in range(N):
    st, end, r = a[i]
    for j in range(M):
        if bank[j] <= st:
            bank[j] = end
            if st <= 1440:
                bankc[j] += 1
                last = st
            break
    else:
        #клиент джет пока не освободится один из банкоматов
        m = min(bank)
        for j in range(M):
            if bank[j] == m:
                if bank[j] <= 1440:
                    bankc[j] += 1
                    last = bank[j]
                bank[j] = bank[j] + r
                break
print(max(bankc), last)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('26-111.txt')                     # две парковки

N, L, M = map(int, f.readline().split())
a = []
for i in range(N):
    st, r , t = f.readline().split()
    a.append([int(st), int(st) + int(r), t])
a.sort()
#первые 0....L - 1 - места для легковых
#следующие L...L+M - места для автобусов
park = [0] * (L + M)
bus = 0
uexal = 0
for i in range(N):
    st, end, t = a[i]
    if t == 'A':
        for j in range(L + M):
            if park[j] <= st:
                park[j] = end
                break
        else:
            uexal += 1
    if t == 'B':
        for j in range(L, L + M):
            if park[j] <= st:
                park[j] = end
                bus += 1
                break
        else:
            uexal += 1
print(bus, uexal)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


f = open('26-111.txt')                       #Организация очереди (ожидание + ограничение времени)

M , N = map(int, f.readline().split())

a = []

for i in range(N):
    st , r = map(int, f.readline().split())
    a.append([st, st + r, r])

a.sort(key = lambda x: x[0])

bank = [0] * M
bankc = [0] * M
last = 0
for i in range(N):
    st, end, r = a[i]
    for j in range(M):
        if bank[j] <= st:
            bank[j] = end
            if st <= 1440:
                bankc[j] += 1
                last = st
            break
    else:
        #клиент джет пока не освободится один из банкоматов
        m = min(bank)
        for j in range(M):
            if bank[j] == m:
                if bank[j] <= 1440:
                    bankc[j] += 1
                    last = bank[j]
                bank[j] = bank[j] + r
                break
print(max(bankc), last)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


f = open('26-111.txt')                #гномы и котлы Организация очереди (задержка + ограничение времени)

D, P = map(int, f.readline().split())

a = []

for i in range(D):
    st, mana = map(int, f.readline().split())
    if mana > 1:
        a.append([st, st+mana//2, mana//2])

a.sort()
kot = [0] * P
count = 0
maxzel = 0
for i in range(len(a)):
    st, end, zel = a[i]
    for j in range(P):
        if kot[j] <= st:
            kot[j] = end if kot[j] == 0 else end + 2
            if kot[j] > 1440:
                zel -= kot[j] - 1440
            count += zel
            maxzel = max(maxzel, zel)
            break
print(count, maxzel)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


from math import *                              #задача с домиками
f = open('26-111.txt')

K, N = map(int, f.readline().split())
a = []

for i in range(N):
    st, end = map(int, f.readline().split())
    a.append([st, end])
a.sort()
house = [0] * 1000
last = 0
for i in range(N):
    st, end = a[i]
    for j in range(1000):
        if house[j]+ 1 <= st:
            house[j] = end
            last = len([x for x in house if x > st])
            break
house = [x for x in house if x != 0]
print(ceil(len(house)/K), last)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('26-111.txt')        #задача на номера по типу егэ

K, N, M = map(int, f.readline().split())

a = [int(x) for x in f]
a.sort(reverse = 1)
placec = [M] * K
count = 0
for i in range(N):
    k = a[i]
    for j in range(K):
        if placec[j] >= k:
            placec[j] -= k
            count += 1
            break
print(count, sum(placec))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('25.py')       #отбор чисел

s, n = map(int, f.readline().split())

a = [int(x) for x in f]

a.sort()

b = []

while sum(b) + a[0] <= s:
    b.append(a.pop(0))

for i in range(len(a)):
    if sum(b) - b[-1] + a[i] <= s:
        b[-1], a[i] = a[i], b[-1]
print(len(b), b[-1])
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


f = open('324')                          #грузы и масса отбор чисел

n, m = map(int, f.readline().split())

a = sorted([int(x) for x in f])

b = []
for i in range(n):
    if 180 <= a[i] <= 200:
        b.append(a[i])
        a[i] = 0

a = [int(x) for x in a if x != 0]

m = m - sum(b)
c = []

while sum(c) + a[0] <= m:
    c.append(a.pop(0))

c.sort(reverse=1)
for i in range(len(c)):
    for j in range(len(a)):
        if a[j] > c[i] and sum(c) - c[i] + a[j] <= m:
            c[i], a[j] = a[j], c[i]
print(len(b+c), sum(b+c))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('324')                         # диски и отбор чисел

v, K, n = map(int, f.readline().split())

a = [int(x) for x in f]
a.sort(reverse=1)

b = [0]*K
t = []
k = 0
for i in range(n):
    for j in range(k, k + K):
        if b[j%K] + a[i]<= v:             # чтобы учесть круговую смену индексов при превышении длины списка b
            b[j%K] += a[i]
            k = j + 1
            break
    else:
        t.append(a[i])
print(sum(t), len(t))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('20342')
n = int(f.readline())
a = [int(x) for x in f]

b = set(a)               # множество
ans = []
for i in range(n):           #перебор пар
    for j in range(i + 1, n):#без повторов
        if (a[i] + a[j]) % 2 == 0:
            sr = (a[i] + a[j]) // 2
            if sr in b:        # через множество потому что много чисел
                ans.append(sr)
print(len(ans), max(ans))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


f = open('3242')         # чекаем кол во чисел и находим пловину
n = int(f.readline())
a = [int(x) for x in f]

a.sort()

ans = []
for i in range(n):
    for j in range(i + 1, n):
        if ((a[i] + a[j]) % 2 == 0):
            sr = a[i] + a[j] // 2
            if sr < a[2500]:
                ans.append(sr)
print(len(ans), max(ans))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from bisect import * # бинарный поиск
f = open('234234')

n = int(f.readline())

a = [int(x) for x in f]

a.sort()
ans = []

for i in range(n):
    for j in range(i + 1, n):
        sr = (a[i]+a[j]) //2
        count = bisect_left(a, sr)           # <= kajf
        if count % 100 == 0:
            ans.append(count)
print(len(ans), max(ans))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('26-111.txt')                # хронология

n = int(f.readline())

a = [0] * 2000001

for i in range(n):
    st, end = map(int, f.readline().split())
    a[st] += 1
    a[end] -= 1

k = 0
count, mx = 0, 0
st, end = -1, 0
for i in range(2_000_001):
    k0 = k
    k += a[i]
    if k == 0 and st == -1: st = i
    if k0 == 0 and (k > 0 or i == 2000000):
        end = i
        count += 1
        mx = max(mx, end-st)
        st , end = -1, 0
print(count, mx)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


f = open('falsdkjf')         # хронология с этапами и много условий

l, n, m = map(int, f.readline().split())

road = [0]*l+1

for i in range(n):
    x, h = map(int, f.readline().split())
    road[x - h//2] += 1
    road[x + h//2] -= 1

lamp = [int(x) for x in f]

dark = []
k = 0
st, end = - 1, 0
for i in range(l + 1):
    k0 = k
    k += road[i]
    if k == 0 and st == -1: st = i
    if k0 == 0 and (k > 0 or i == l):
        end = i
        dark.append(end - st)
        st, end = -1, 0

dark.sort()
lamp.sort()
s, over = 0, 0
for i in range(len(dark)):
    for j in range(len(lamp)):
        if lamp[j] >= dark[i]:
            s += lamp[j]
            over += lamp[j] - dark[i]
            lamp[j] = 0
            break
print(s, over)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('34235')
n , k = map(int, f.readline().split())
d = 24 * 3600 * 1000
ST = k
END = k + d
a = [0] * (d + 1)
for i in range(n):
    st, end = map(int, f.readline().split())
    if (st < END or st == 0) and (end > ST or end == 0):
        if st < ST or st == 0: st = ST
        if end > END or end == 0: end = END
        a[st - ST] += 1
        a[end - ST] -= 1

k = 0
mx = 0
count = 0
for i in range(d+1):
    k+= a[i]
    if k > mx: mx, count = k, 0
    if k == mx: count += 1
print(mx, count)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f = open('26-111.txt')

s, n = map(int, f.readline().split())

a = [int(x) for x in f]                   #запись на диск
a.sort()
b = []

while sum(b) + a[0] <= s:
    for i in range(len(a) - 1, 0, -1):
        if sum(b) + a[i] <= s:
            b += [a.pop(i)]
            break
    if sum(b) + a[0] <= s:
        b += [a.pop(0)]
print(len(b), b[-1])
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



