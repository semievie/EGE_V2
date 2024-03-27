count = 0
for line in open('9.txt'):
    a = list(map(int, line.split()))
    if len(a) == len(set(a)):
        if 3 * (max(a) + min(a)) <= 2 * (sum(a) - (max(a) + min(a))):
            count += 1
print(count)
----------------------------------------------------------------------------------------------------------------

f = open('24_2250.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0] + a[4]) ** 2 > a[1]**2 + a[2]**2 + a[3]**2:
        k += 1
print(k)
----------------------------------------------------------------------------------------------------------------


k = 0
for s in open('09032'):
    a = sorted([int(x) for x in s.split()])
    if a[3] < a[0] + a[1] + a[2] and a[0] + a[3] == a[1] + a[2]:
        k += 1
print(k)
----------------------------------------------------------------------------------------------------------------

k = 0
for s in open('9.txt'):
    a = [int(x) for x in s.split()]
    a3 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 3 and len(a1) == 3 and 3*sum(a1) <= a3[0]**3:
        k += 1

print(k)
----------------------------------------------------------------------------------------------------------------


k = 0
for s in open('9.txt'):
    a = sorted([int(x) for x in s.split()])
    if a[0] == a[1] and a[2] == a[3] and a[4] == [5]:
        k += 1
print(k)
----------------------------------------------------------------------------------------------------------------

k = 0

for s in open('932948'):
    a = [int(x) for x in s.split()]
    a2 = [x for x in a if a.count(x) > 1]
    a1 = [x for x in a if x % 2 != 0]
    if (len(a2)) > 0 + (len(a1) == 3) == 1:
        k += 1
print(k)
----------------------------------------------------------------------------------------------------------------


k = 0

for s in open('fljdfl'):
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x) > 1]
    a2 = [x for x in a if x% 2 == 0 ]
    a3 = [x for x in a if x % 2 != 0]
    if len(a2) == 0 and len(a2) < len(a3) and sum(a2) > sum(a3):
        k += 1
print(k)
----------------------------------------------------------------------------------------------------------------

k = 0

for s in open('0230'):
    a = sorted([int(x) for x in s.split()])
    a2 = [x for x in a if a.count(x) > 1]
    if a.count(a[0]) == 1 and len(a2) > 0 and a[0] + a[5] < (a[1] + a[2] + a[3] + a[4]) / 2:
        k += 1
print(k)
----------------------------------------------------------------------------------------------------------------

#строки
k = 0
for s in open('0932'):
    k += 1
    a = [int(x) for x in s.split()]
    a2 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2) == 2 and len(a1) == 4 and a2[0] >= sum(a1) / 4:
        print(k)
----------------------------------------------------------------------------------------------------------------


k = 0
for s in open('0002'):
    a = sorted([int(x) for x in s.split()])
    a2 = [x for x in a if a.count(x) == 2]
    a3 = [x for x in a if a.count(x) == 1]
    if len(a2) == 4 and len(a3) == 3 and a[6] != a[5]:
        print(sum(a))
        break
----------------------------------------------------------------------------------------------------------------

ans = 0
for s in open('9.txt'):
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x) == 3]
    a2 = [x for x in a if a.count(x) == 2]
    a3 = [x for x in a if a.count(x) == 1]
    if len(a1) == 3 and len(a2) == 4:
        ost = [x % 2 for x in a[4:]] # пары с нечетными суммами
        if ost.count(1) == 2:
            ans += sum(a)
print(ans)
----------------------------------------------------------------------------------------------------------------
