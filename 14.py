for x in range(21):
    for y in range(21):
        f1 = 9 * 21 ** 8 + 4 * 21 ** 7 + 3 * 21 ** 6 + 6 * 21 ** 5 + 9 * 21 ** 4 + 7 * 21 ** 3 + x * 21 ** 2 + 2 * 21 ** 1 + 1 * 21 ** 0
        f2 = 2 * 21 ** 5 + y * 21 ** 4 + 9 * 21 ** 3 + 2 * 21 ** 2 + 5 * 21 ** 1 + 3 * 21 ** 0
        f = f1 - f2
        if f % 20 == 0:
            print(f // 20, x-y)