f = [0] * 3017

for n in range(0, 3016):
    if n <7:    f[n] = 7
    if n >= 7 and n % 3 != 0:   f[n] = 5 - f[n-1]
    if n >= 7 and n % 3 == 0:   f[n] = 3 + f[n-1]

print(f[3015])