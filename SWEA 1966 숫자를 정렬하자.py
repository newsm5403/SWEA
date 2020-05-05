for i in range(int(input())):
    input()
    print(f'#{i+1}', end=" ")
    a = list(map(int, input().split()))
    a.sort()
    for j in range(len(a)):
        print(f'{a[j]}', end=" ")
    print()