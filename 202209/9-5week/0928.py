# https://www.acmicpc.net/problem/1541

n = input().split('-')
list = []

for i in n :
    temp = 0
    x = i.split('+')
    for j in x :
        temp += int(j)
    list.append(temp)
y = list[0]

for i in range(1, len(list)) :
    y -= list[i]

print(y)