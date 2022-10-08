# https://www.acmicpc.net/problem/1389

import sys
from collections import deque

def bfs(realationship, sNode):
    num = [0] * (N + 1)
    queue = deque([sNode])
    visited[sNode] = 1

    while queue:
        node = queue.popleft()

        for i in realationship[node]:
            if not visited[i]:
                num[i] = num[node] + 1
                queue.append(i)
                visited[i] = 1
    res = sum(num)

    return res


N, M = map(int, sys.stdin.readline().split())
realationship = [[] for i in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    realationship[A].append(B)
    realationship[B].append(A)

result = []
for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    result.append(bfs(realationship, i))

print(result.index(min(result)) + 1)