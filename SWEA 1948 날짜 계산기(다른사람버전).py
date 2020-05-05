l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    print(f'#{i + 1} {d - b + 1 + sum(l[a - 1:c - 1])}')
