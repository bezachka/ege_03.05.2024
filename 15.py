for a in range(10000):
    flag = 1
    for x in range(200):
        for y in range(200):
            f = ((a < x) or ((x**2 - 7*x + 10) > 0)) and ((a >= y) or ((y**2 + 7*y + 12) > 0))
            if f == False:
                flag = 0
                break
    if flag == 1:
        print(a)