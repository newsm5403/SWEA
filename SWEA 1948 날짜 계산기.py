for i in range(int(input())):
    a = list(map(int, input().split()))
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a[2] == a[0]:
        print(f'#{i + 1} {a[3] - a[1] + 1}')
    else:
        print(f'#{i + 1} {m[a[0] - 1] - a[1] + 1 + a[3] + sum(m[a[0]:a[2] - 1])}')
