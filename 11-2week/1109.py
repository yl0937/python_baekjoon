# https://www.acmicpc.net/problem/9019
import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int,sys.stdin.readline().split())
    que = deque()
    que.append([a,""])
    visited = [0 for _ in range(10000)]

    while que:
        num, path = que.popleft()
        visited[num] = 1
        if num == b:
            print(path)
            break

        num2 = (2*num)%10000
        if visited[num2]==0:
            que.append((num2,path+"D"))
            visited[num2] = 1
        num2 = (num-1)%10000
        if visited[num2] == 0:
            que.append((num2,path+"S"))
            visited[num2] = 1
        num2 = (10*num+(num//1000))%10000
        if visited[num2] == 0:
            que.append((num2,path+"L"))
            visited[num2] = 1
        num2 = (num//10+(num%10)*1000)%10000
        if visited[num2] == 0:
            que.append((num2,path+"R"))
            visited[num2] = 1
