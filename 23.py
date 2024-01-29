def f(x, end):
    if x > end or x == 13: return 0
    if x == end: return 1
    return f(x + 1, end) + f(x + 2, end) + f(x * 3, end)

print(f(3,8) * f(8, 18))




def f(x, end, flag):
    if x > end: return 0
    if x == end: return 1
    elif flag:
        return f(x + 1, end, True) + f(x + 2, end, True) + f(x * 2, end, False)
    else:
        return f(x + 1, end, True) + f(x + 2, end, True)
print(f(1,11, True))
