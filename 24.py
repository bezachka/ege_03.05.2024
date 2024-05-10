f = open('24_16269.txt').readline().replace('ZZZZ', 'ZZ*ZZ').replace('XXXX', 'XX*XX').replace('YYYY', 'YY*YY').replace('XXX', 'XX*XX').replace('YYY', 'YY*YY').replace('ZZZ', 'ZZ*ZZ').replace('XX', 'H').replace('YY', 'K').replace('ZZ', 'L')
f = f.replace('HH', 'H*H').replace('KK', 'K*K').replace('LL', 'L*L').split('*')
print(f)


a = max(list(map(len, f)))

for i in range(len(f)):

    if len(f[i]) == 31:
        print(f[i]) #KHLHKLHKLHLKHKHKHKLHKHKLKL(сумма: 26 *2 = 52) (v - лишнее) VLHKL
print(a)