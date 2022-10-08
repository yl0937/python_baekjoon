# https://www.acmicpc.net/problem/1107

number = int(input())
res = abs(100 - number)
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        res = min(res, len(str(num)) + abs(num - number))

print(res)