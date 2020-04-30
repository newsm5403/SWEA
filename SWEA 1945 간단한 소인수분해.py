for T in range(int(input())):
    N = int(input())
    t = ''
    for i in (2, 3, 5, 7, 11):
        d = 0
        while N % i == 0:
            d += 1
            N /= i
        t += str(d) + ' '
    print(f'#{T + 1} {t}')
