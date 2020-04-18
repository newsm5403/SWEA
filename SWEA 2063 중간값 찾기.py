N = int(input())
a = [int(i) for i in input().split()]
a.sort()
print(a[N // 2])
