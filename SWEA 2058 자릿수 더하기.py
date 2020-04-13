N = int(input())  # 정수형 입력받기
dummy = N
sum_N = 0
i = 3
while i >= 0:
    sum_N += dummy // pow(10,i)
    dummy = N % pow(10,i)
    i -= 1
print(sum_N)
