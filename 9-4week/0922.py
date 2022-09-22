# https://www.acmicpc.net/problem/1012

n = int(input())
for i in range(0,n):
    num = input().split()
    array = [[0 for col in range(int(num[0]))] for row in range(int(num[1]))]
    for h in range(0,int(num[2])):
        cabbage = input().split()
        # 상
        if(int(cabbage[0])>0):
            if(array[int(cabbage[0])-1][int(cabbage[1])]==1):
                array[int(cabbage[0])][int(cabbage[1])] = 2
        # 하
        elif (int(cabbage[0]) < int(num[2])-1):
            if (array[int(cabbage[0]) + 1][int(cabbage[1])] == 1):
                array[int(cabbage[0])][int(cabbage[1])] = 2
        # 좌
        elif (int(cabbage[1]) > 0):
            if (array[int(cabbage[0])][int(cabbage[1])-1] == 1):
                array[int(cabbage[0])][int(cabbage[1])] = 2

        # 우
        elif (int(cabbage[1]) < int(num[0])-1):
            if (array[int(cabbage[0]) - 1][int(cabbage[1])+1] == 1):
                array[int(cabbage[0])][int(cabbage[1])] = 2
        else:
            array[int(cabbage[0])][int(cabbage[1])] = 1
    print(array)
