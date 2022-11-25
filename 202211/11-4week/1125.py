# https://www.acmicpc.net/problem/1654

import sys

K , N = map(int,input().split())
lan = [int(sys.stdin.readline()) for i in range(K)]

start = 1
end = max(lan)
while(end>=start):
    mid = (start + end) // 2
    count = 0
    for i in lan:
        count += i // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)