def f(n):
    if n >= 2025: return n
    if n < 2025: return n + 3 + f(n + 3)
print(f(23) - f(21))



# с превышением рекурсии
from sys import *
setrecursionlimit(10000)

def f(n):
    if n >= 2025: return n
    if n < 2025: return n + 3 + f(n + 3)
print(f(23) - f(21))