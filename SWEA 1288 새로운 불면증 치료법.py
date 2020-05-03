for i in range(int(input())):
    N = int(input())
    Set = set(str(N))
    count = 1
    while len(Set) < 10:  # while len(Set) 세트의 길이(문자수)가 0부터 9까지가 아니라면 while 문 수행
        count += 1
        Set.update(set(str(N * count)))  # update 함수는 set 와 set 를 합칠 수 있음!! 하지만 add()함수는 불가능!
    print(f'#{i + 1} {N * count}')
