# https://www.acmicpc.net/problem/9375

from collections import Counter

T = int(input())
for i in range(T):
    n = int(input())
    wear = []
    for h in range(n):
        name,type = map(str,input().split())
        wear.append(type)

    wearCase = Counter(wear)
    case = 1

    for item in wearCase:
        case *= wearCase[item] + 1
    print(case-1)

