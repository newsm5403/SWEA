for i in range(int(input())):
    input()
    result = 0
    r = []
    a, b = map(lambda x: x.split(), (input(), input()))
    if len(a) > len(b):
        a, b = b, a
    while len(b) > len(a) - 1:
        r.append(sum([int(t[0]) * int(t[1]) for t in zip(a, b)]))
        b.pop(0)
    print(f'#{i + 1} {max(r)}')
