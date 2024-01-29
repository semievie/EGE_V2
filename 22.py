time = {'0': 0}

for s in open('22.txt'):
    s = s.replace(';', ' ')
    s = s.split()
    time[s[0]] = int(s[1]) + max(time[k] for k in s[2:])

print(max(time.values()))