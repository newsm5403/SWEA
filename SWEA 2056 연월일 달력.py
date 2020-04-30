T = int(input())
for i in range(1, T + 1):
    A = input()
    year = int(A[0:4])
    month = int(A[4:6])
    day = int(A[6:9])
    if month <= 0 or month > 12:
        print("#{} {}".format(i, -1))
    elif day <= 0:
        print("#{} {}".format(i, -1))
    elif month == 2 and day > 28:
        print("#{} {}".format(i, -1))
    elif (month == 4 or 6 or 9 or 11) and day > 30:
        print("#{} {}".format(i, -1))
    elif day > 31:
        print("#{} {}".format(i, -1))
    else:
        print("#{} {}/{}/{}".format(i, A[0:4], A[4:6],A[6:9]))
