a = [int(x) for x in open('17.txt')]

ans = []

for i in range(len(a)):
    if (a[i] % 10 == 2 or a[i] % 10 == 7) and a[i] % 3 == 0 and a[i] % 11 == 0:
        ans.append(a[i])
print(len(ans), min(ans))


a = [int(c) for c in open('17.txt')] #пар элементов последовательности

ans = []

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] + a[j]) % 60 == 0) and ((a[i] % 40 == 0) or (a[j] % 40 == 0)):
            ans.append(a[i] + a[i])
print(len(ans), max(ans))


