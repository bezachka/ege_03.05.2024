f = [int(i) for i in open('17_16264.txt')]
sp = []
for i in f:
    k = str(i)
    if len(k) == 2:
        if i % (int(k[0]) + int(k[-1])) == 0:
            sp.append(i)
count = 0
print(sp)
h = (min(sp))
ms = -10000

for i in range(len(f) - 1):
    if f[i] % h == 0 or f[i+1] % h == 0:
        count += 1
        ms = max(ms, f[i] + f[i + 1])

print(count, ms)
