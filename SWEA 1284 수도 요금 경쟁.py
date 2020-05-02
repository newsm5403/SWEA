for i in range(int(input())):
    a = list(map(int, input().split()))
    SUM1 = a[4] * a[0]
    if a[4] > a[2]:
        SUM2 = a[1] + (a[4] - a[2]) * a[3]
    else:
        SUM2 = a[1]
    if SUM1 > SUM2:
        SUM = SUM2
    elif SUM2 > SUM1:
        SUM = SUM1
    print(f'#{i+1} {SUM}')