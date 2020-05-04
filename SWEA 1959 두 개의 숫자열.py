for i in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))  # a, b = map(lambda x: x.split(), (input(), input())) 로 대체 가능
    B = list(map(int, input().split()))
    SUM = [0 for _ in range(abs(N - M) + 1)]
    """
    C = A
    if N > M:
        A = B
        B = C
    else:
        pass"""
    if N > M:
        A, B = B, A
    for j in range(abs(N - M) + 1):  # 배열 숫자가 작은 건 j에 영향을 받음
        for k in range(min(N, M)):  # 덧셈 횟수에 영향을 줌
            SUM[j] += B[k + j] * A[k]
    print(f'#{i + 1} {max(SUM)}')
