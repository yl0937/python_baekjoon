# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10**6)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    array[x][y] = 0
    for t in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= int(num[1]) or ny < 0 or ny >= int(num[0]):
            continue
        if array[nx][ny] == 1:
            dfs(nx, ny)
    return

n = int(input())
for i in range(0,n):
    num = input().split()
    array = [[0 for col in range(int(num[0]))] for row in range(int(num[1]))]
    for j in range(0,int(num[2])):
        cabbage = input().split()
        x = int(cabbage[0])
        y = int(cabbage[1])
        array[y][x] = 1
    warm = 0
    for g in range(int(num[1])):
        for h in range(int(num[0])):
            if array[g][h] ==1:
                dfs(g,h)
                warm += 1
    print(warm)
