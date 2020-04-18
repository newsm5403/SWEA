A, B = map(int, input().split())
if round((A+1) % 3.1) == B:
    print('B')
else:
    print('A')