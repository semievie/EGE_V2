s = open('24_2422.txt').readline()

c = m = 1
for i in range(len(s) - 1):
    if s[i] <= s[i+ 1]:
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)
----------------------------------------------------------------------------------------------------------------

s = open('24_2427.txt').readline()
c = m = s[0]#последовательность символов в убывающем порядке

for i in range(1, len(s)):
    if s[i - 1] > s[i]:
        c += s[i]
        m = max(m, c, key=len)
    else:
        c = s[i]
print(m)
----------------------------------------------------------------------------------------------------------------

s = open('als;dkjf').readline()
s = s.replace('A', ' ').replace('A', ' ')       # <= дефолт разделение и поиск макс
print(max(len(c) for c in s.split()))
----------------------------------------------------------------------------------------------------------------

s = open('23042034').readline()

for c in 'qwrtyuiopsghjklzxvbnm':        # <= весь алфавит и провеить в 16 системе
    s = s.replace(c, ' ')

print(max(len(c) for c in s.split()))

----------------------------------------------------------------------------------------------------------------

s = open('24234').readline()
s = s.replace('ST', 'S T')   # <= условаие запрещает ST в последовательности
print(max(len(c) for c in s.split()))

----------------------------------------------------------------------------------------------------------------

s = open('243234').readline()
s = s.replace('KEGE', 'KEG EGE')  # <= замена целового слова и как оно разбивается
print(max(len(c) for c in s.split()))

----------------------------------------------------------------------------------------------------------------

s = open('234234').readline()
while 'PPP' in s: s = s.replace('PPP', 'PP PP')
print(max(len(c) for c in s.split()))
----------------------------------------------------------------------------------------------------------------

s = open('al;kdsfjlsf').readline()

s = s.replace('ZX', '*').replace('ZY', '*')  # <= пары замена
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(max(len(c) for c in s.split()))

----------------------------------------------------------------------------------------------------------------

s = open('24_2250.txt').readline()

s = s.replace('B', 'A').replace('C', 'A')
s = s.replace('2', '1').replace('3', '1')   # <= подряд тройки вида "буква + цифра + цирфа"
s = s.replace('A11', '*').replace('A', ' ').replace('1', ' ')
print(max(len(c) for c in s.split()))
----------------------------------------------------------------------------------------------------------------

s = open('24_2250.txt').readline()

s = s.replace('B', 'A').replace('C', 'A')
s = s.replace('8', '9')
while 'AA' in s: s = s.replace('AA', 'A A') # <= никакая буква не должна идти подряд за буквой также и с цифрмами
while '99' in s: s = s.replace('99', '9 9')
print(max(len(c) for c in s.split()))

----------------------------------------------------------------------------------------------------------------
s = open('24_2250.txt').readline()
#поиск максильмального с буквами А не более 3
s = s.split('A')
m = 0
for i in range(len(s) - 3):
    c = s[i] + 'A' + s[i + 1] + 'A' + s[i + 2] + 'A' + s[i + 3]
    # если букв много
    # с = 'A'.join(s[i:i + ..])
    m = max(m, len(c))
print(m)

s = open('24_2250 (1).txt').readline()

s = s.split('A')
m = 0

for i in range(len(s) - 1):
    c = s[i] + 'A' + s[i + 1]
    m = max(m, len(c))
print(m)
----------------------------------------------------------------------------------------------------------------
s = open('234234234').readline()

s = s.split('A')
m = 10000
for i in range(len(s) - 35):
    #склеиваете 36 кусков
    c = 'A'.join(s[i:i+36])
    m = min(m , len(c) - len(s[i]) - len(s[i + 35]))
print(m)

----------------------------------------------------------------------------------------------------------------
s = open('24_2422 (2).txt').readline()
sub = s[0]
m = 0
for i in range(1, len(s)):   # алфавитный порядок
    if s[i] >= s[i - 1]:
        sub += s[i]
        m = max(m, len(sub))
    else:
        sub = s[i]
print(m)
----------------------------------------------------------------------------------------------------------------
#динамический подсчет
s = open('lasjdkflasjdf').readline()

m = [0] * len(s)

for i in range(len(s)):
    if s[i] in 'ACDF':
        m[i] = m[i - 1] + 1
print(max(m))
----------------------------------------------------------------------------------------------------------------
#каждые два соседних различны
s = open('al;sjkdflsjf)').readline()

m = [1] * len(s)

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        m[i] = m[i - 1] + 1
print(max(m))
----------------------------------------------------------------------------------------------------------------
s = open('24_4546.txt').readline()
m = 0
for i in range(3):
    c = 0
    for j in range(i, len(s) - 2, 3):
        if s[j] + s[j + 2] == 'AA' or s[j] + s[j + 2] == 'CC':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
----------------------------------------------------------------------------------------------------------------
s = open('24_2425.txt').readline()  #лайфкак перебора 24 с повтором

c = 'DBAC' * 23 + 'DBA'
print(len(c))
----------------------------------------------------------------------------------------------------------------

s = open('24_66.txt').readline()            #найти максимальную последовательность комбинации слова КОТ

s = s.replace('KOT', '*')
s = s.replace('K', ' ').replace('O', ' ').replace('T', ' ')
print(max(len(c) for c in s.split()))