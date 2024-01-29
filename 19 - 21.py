# с одной кучой
def f(a, m):
    if a >= 52: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1, m - 1), f(a + 10, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print('19)', [s for s in range(1, 51) if f(s, 2)]) # all => any если первый ход проигрышный 100%
print('20)', [s for s in range(1, 51) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 51) if not f(s, 2) and f(s, 4)])


#с двумя кучами
def f(a,b, m):
    if a + b >= 52: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1,b, m - 1), f(a + 10, b, m - 1),f(a ,b + 1, m - 1), f(a, b + 10, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print('19)', [s for s in range(1, 51) if f(5, s, 2)]) # all => any если первый ход проигрышный 100%
print('20)', [s for s in range(1, 51) if not f(5, s, 1) and f(5, s, 3)])
print('21)', [s for s in range(1, 51) if not f(5, s, 2) and f(5, s, 4)])


#предыдущие ходы испльзовать нельзя
def f(s, m, p):
    if s >= 140: return m%2 == 0
    if m == 0: return 0
    h = []
    if p != '+1': h += [f(s + 1, m - 1, '+1')]
    if p != '+2': h += [f(s + 2, m - 1, '+2')]
    if p != '*3': h += [f(s * 3, m - 1, '*3')]
    return any(h) if m % 2 != 0 else all(h)
print([s for s in range(1,140) if f(s, 2, '')])
print([s for s in range(1,140) if not f(s, 1, '') and f(s, 3, '')])
print([s for s in range(1,140) if not f(s, 2, '') and f(s, 4, '')])

#нельзя повторять СВОЙ предыдущий ход
def f(s, m, p1, p2):
    if s >= 121: return m % 2 == 0
    if m == 0: return 0
    h = []
    if p2 != '+2': h += [f(s + 2, m - 1, '+2', p1)]
    if p2 != '+5': h += [f(s + 5, m - 1, '+5', p1)]
    if p2 != '+12': h += [f(s + 12, m - 1, '+12', p1)]
    if p2 != '*2': h += [f(s * 2, m - 1, '*2', p1)]
    return any(h) if m % 2 != 0 else all(h)
print([s for s in range(1,120) if f(s, 2, '', '')])
print([s for s in range(1,120) if not f(s, 1, '', '') and f(s, 3, '', '')])
