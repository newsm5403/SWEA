for t in range(int(input())):
    P, Q, R, S, W = map(int,input().split())
    print(f'#{t+1}', min(W*P, Q+max(0, (W-R)*S)))