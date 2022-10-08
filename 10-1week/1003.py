# https://www.acmicpc.net/problem/1780

N = int(input())

paper = [list(map(int, input().split())) for i in range(0,N)]

minus = 0
zero = 0
plus = 0


def division(x, y, n):
    global minus, zero, plus

    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (paper[i][j] != num_check):
                for k in range(0,3):
                    for l in range(0,3):
                        division(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if (num_check == -1):
        minus += 1
    elif (num_check == 0):
        zero += 1
    else:
        plus += 1


division(0, 0, N)
print(f'{minus}\n{zero}\n{plus}')