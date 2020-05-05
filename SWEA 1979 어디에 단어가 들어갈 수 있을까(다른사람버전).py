for i in range(int(input())):
    N, K = map(int, input().split())
    a = [''.join(input().split()) for _ in range(N)]
    b = [''.join(i) for i in zip(*a)]  # 같은 리스트 안에 있는 리스트의 index 로 묶고 싶다면 zip(*x)를 이용할 것!
    count = 0
    for j in (a, b):  # j 안에 a, b를 집어넣음
        for k in j:  # k 안에 a[0] .. a[끝] -> b[0] .. b[끝] 순으로 집어넣음
            count += k.split('0').count('1' * K)
    print(f'#{i + 1} {count}')
