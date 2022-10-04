# https://www.acmicpc.net/problem/1003

n = int(input())

for i in range(0,n):
    zero = [1, 0]
    one = [0, 1]
    num = int(input())
    if num > 1:
        for h in range(0,num - 1):
            # 이전 1의 개수
            zero.append(one[-1])
            # 이전 0의 개수 + 이전 1의 개수
            one.append(zero[-2] + one[-1])

    print(zero[num], one[num])