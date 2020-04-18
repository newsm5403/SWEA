T = int(input())
A = [0 for i in range(T)]
B = [0 for i in range(T)]
for i in range(T):
    A[i], B[i] = map(int, input().split())
for k in range(T):
    print("#{} {} {}".format(k+1, A[k] // B[k], A[k] % B[k]))