for n in range(1,100):
    b = bin(n)[2:]
    b += b[-1]
    b += '0' if b.count('1') % 2 == 0 else '1'
    b += '0' if b.count('1') % 2 == 0 else '1'
    r = int(b, 2)
    if r > 144:
        print(r)
----------------------------------------------------------------------------------------------------------------
#def s2(x): Перевод в разные системы счисления
 #   s = ''
  #  while x > 0:
    #    s = str(x % 3) + s
    #    x //= 3
  #  return s
----------------------------------------------------------------------------------------------------------------
for n in range(100,1000):
    b = [int(x) for x in str(n)]
    s1 = b[0] + b[1]
    s2 = b[1] + b[2]
    if s1 > s2:
        r = str(s1) + str(s2)
    else:
        r = str(s2) + str(s1)
    if r == '159':
        print(n)
----------------------------------------------------------------------------------------------------------------
# c подвохом и добавлением массива я в ахуе!!!
mas = []
for n in range(1,40000):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b[:3] + b
    else:
        s = n % 3 * 5
        c = bin(s)[2:]
        b = b + c
    r = int(b, 2)
    if r > 39000 and r < 39018:
        mas.append(r)
print(min(mas))
----------------------------------------------------------------------------------------------------------------
def s2(x):            #использование другой системы счисления
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s
for n in range(1,100):
    b = s2(n) + str(n % 3)
    r = int(b, 3)
    if r > 99:
        print(r)

----------------------------------------------------------------------------------------------------------------