for i in range(int(input())):
    N = int(input())
    SUM = 0
    for j in range(1, N + 1):
        if j % 2 == 0:
            SUM -= j
        else:
            SUM += j
    print(f'#{i+1} {SUM}')
