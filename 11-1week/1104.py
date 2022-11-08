# Preorder
arr = ['A','B','C','D','E','F','G','H','I','J']
result1 = []
result2 = []
result3 = []
def preOreder(n):
    left = (n * 2) + 1
    right = (n * 4) + 2
    result1.append(str(arr[n]))
    if(left<len(arr)):
        preOreder(left)
    if(right<len(arr)):
        preOreder(right)

def inOrder(n):
    left = (n * 2) + 1
    right = (n * 2) + 2
    if(left<len(arr)):
        inOrder(left)
    result2.append(str(arr[n]))
    if(right<len(arr)):
        inOrder(right)

def postOrder(n):
    left = (n * 2) + 1
    right = (n * 2) + 2
    if(left<len(arr)):
        postOrder(left)
    if(right<len(arr)):
        postOrder(right)
    result3.append(str(arr[n]))

print("1.Preorder -------")
preOreder(0)
print(result1)
print("2.inorder -------")
inOrder(0)
print(result2)
print("3.postOrder -------")
postOrder(0)
print(result3)
