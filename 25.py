sp = []

for x in range(10):
    for y in range(10):
        for z in range(10):
            k = f'12{x}345{y}67089{z}'
            if int(k) % 206 == 0:
                sp.append(int(k))

print(sorted(sp))
for i in sp:
    print(i, i // 206)