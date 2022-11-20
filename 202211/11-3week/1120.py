# https://www.acmicpc.net/problem/11047

T = int(input())

for _ in range(T):
    N = input()
    T5 = 5 * (10 ** (len(N) - 1)) - 1  # 49...9
    num_1 = ''
    num_2 = ''

    if int(N) >= T5:
        num_1 = T5 + 1
        num_2 = T5

    else:
        num_1 = int(N)

        for i in N:
            num_2 += str(9 - int(i))
        num_2 = int(num_2)

    print(num_1 * num_2)