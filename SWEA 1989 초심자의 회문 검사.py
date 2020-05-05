for i in range(int(input())):
    a = input()
    n = len(a) // 2
    for j in range(n + 1):
        if a[j] == a[len(a) - 1 - j]:
            continue
        else:
            print(f'#{i + 1} 0')
            break
    if j == n:
        print(f'#{i + 1} 1')
