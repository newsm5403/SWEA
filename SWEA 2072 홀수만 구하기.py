T = int(input())
for i in range(1, T + 1):
    a = list(map(int, input().split()))
    sum = 0
    for k in range(10):
        if a[k] % 2 == 1:
            sum += a[k]
    print("#{} {}".format(i, sum))