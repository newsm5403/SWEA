N = int(input())  # 정수형 입력받기
n = 0
dummy = N
sum_N = 0

while True:       # 정수 자리수 구하기
    result = N // pow(10, n)
    if result == 0:
        break
    n += 1

while n >= 0:     # 정수 자리수 합 구하기
    sum_N += dummy // pow(10, n)
    dummy = N % pow(10, n)
    n -= 1
print(sum_N)
