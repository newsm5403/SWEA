T = int(input())
for i in range(T):
    A = map(int, input().split())
    print("#{} {}".format(i+1, max(A)))
