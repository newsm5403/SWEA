for i in range(int(input())):
    s = input()
    print(f'#{i + 1} {int(s[::-1] == s)}')
    """
    s[::-1]은 s 문자열을 뒤집는 python 에서 자주 쓰이는 방법이다.
    int 를 씌우는 이유는 == 는 Boolean 변수이기 때문이다.
    안쓰면 True 나 False 가 뜬다.
    """
