T = int(input())
for i in range(1, T + 1):
    a = list(map(int, input().split()))
    SUM = sum(a)
    print("#{} {}".format(i, round(SUM / 10)))
