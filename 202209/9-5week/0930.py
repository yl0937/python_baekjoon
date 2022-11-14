# https://www.acmicpc.net/problem/1676

import sys

n = int(sys.stdin.readline())
num = 1

for i in range(1,n+1):
    num *= i
count = 0

for j in reversed(list(str(num))):
    if j == '0':
        count +=1
    else:
        break
print(count)