for x in '0123456789abcde':
    s = int('97968' + x + '13', 15) + int('7' + x + '213', 15)
    if s % 14 == 0:
        print(x, s // 14)