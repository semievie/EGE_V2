def f(x, A):
    return (x & 39 == 0) or ((x & 11 == 0) <= (x & A != 0))
for a in range(1,1000):
    if all(f(x, a) == 1 for x in range(1,1000)):
        print(a)