class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def insert(self,data):
        self.heap.append(data)

        cur = len(self.heap) - 1
        while(cur > 1 and self.heap[int(cur/2)] > self.heap[cur]):
            parentVal = self.heap[int(cur/2)]
            self.heap[int(cur/2)] = self.heap[cur]
            self.heap[cur] = parentVal

            cur = int(cur/2)
    def delete(self):
        if(len(self.heap)==1):
            print("Heap is empty")
            return 0

        target = self.heap[1]

        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap.remove(self.heap[len(self.heap) - 1])

        cur = 1
        while(True):
            leftIdx = cur * 2
            rightIdx = cur * 2 + 1
            targetIdx = -1

            if (rightIdx < len(self.heap)):
                if(self.heap[leftIdx] < self.heap[rightIdx]):
                    targetIdx = leftIdx
                else:
                    targetIdx = rightIdx
            elif (leftIdx < len(self.heap)):
                targetIdx = cur * 2
            else: break

            if(self.heap[cur] < self.heap[targetIdx]):
                break
            else:
                parentVal = self.heap[cur]
                self.heap[cur] = self.heap[targetIdx]
                self.heap[targetIdx] = parentVal
                cur = targetIdx

        return target

    def printTree(self):
        res = ""
        for i in range(1,len(self.heap)):
            res += str(self.heap[i]) +  " "
        print(res)


minHeap = Heap()
print("데이터 삽입")
minHeap.insert(30)
minHeap.insert(40)
minHeap.insert(10)
minHeap.printTree()
minHeap.insert(50)
minHeap.insert(60)
minHeap.insert(70)
minHeap.printTree()
minHeap.insert(20)
minHeap.printTree()
minHeap.insert(30)
minHeap.printTree()
print("데이터 삭제: ",minHeap.delete())
minHeap.printTree()
print("데이터 삭제: ",minHeap.delete())
minHeap.printTree()
print("데이터 삭제: ",minHeap.delete())
minHeap.printTree()