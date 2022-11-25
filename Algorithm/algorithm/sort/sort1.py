# 1. bubble sort

def bubbleSort(arr):
    for i in range(1,len(arr)-1):
        for j in range(0,len(arr)-i):
            if(arr[j] > arr[j+1]):
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

def bubbleSort2(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if (arr[j] > arr[j + 1]):
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

# 2. Insertion Sort

def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if(arr[j] < arr[j-1]):
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
            else: break

    return arr

# 3. SelectionSort

def selectionSort(arr):
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i +1 ,len(arr)):
            if(arr[j] < arr[min]):
                min = j
        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp

    return arr

def selectionSort2(arr):
    for i in range(len(arr)-1,0,-1):
        max = i
        for j in range(i-1,-1,-1):
            if(arr[j] > arr[max]):
                max = j
        tmp = arr[i]
        arr[i] = arr[max]
        arr[max] = tmp

    return arr

# test
arr = [3,5,2,7,1,4]
print(" 버블 정렬 1 : ", bubbleSort(arr))
arr = [3,5,2,7,1,4]
print(" 버블 정렬 2 : ", bubbleSort2(arr))
arr = [3,5,2,7,1,4]
print(" 삽입 정렬 1 : ", insertionSort(arr))
arr = [3,5,2,7,1,4]
print(" 선택 정렬 1 : ", selectionSort(arr))
arr = [3,5,2,7,1,4]
print(" 선택 정렬 2 : ", selectionSort2(arr))