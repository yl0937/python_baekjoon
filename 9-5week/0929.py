# https://www.acmicpc.net/problem/1620

import sys

n, m = map(int, input().split())

intKey = {}
nameKey = {}
for i in range(0,n):
    name = sys.stdin.readline().strip()
    intKey[i] = name
    nameKey[name] = i

for i in range(0,m):
    question = sys.stdin.readline().strip()
    if question.isdigit() == True:
        print(intKey[int(question)-1])
    else:
        print(nameKey[question]+1)