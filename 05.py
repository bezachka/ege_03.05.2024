def f(n):
    ost = ''
    while n != 0:
        ost = str(n % 3) + ost
        n = n // 3

    return ost
sp = []
for n in range(1,200):
    n3 = f(n)
    if n % 2 == 0:
        n3 = '2' + n3 + f(int(n3[-1]) * 2)
    else:
        n3 = f(int(n3[0]) * 2) + n3 + '2'

    r = int(n3, 3)
    if r > 100:
        sp.append(r)

print(min(sp))
