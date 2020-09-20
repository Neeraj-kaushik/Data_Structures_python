class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(tree,summax=0,nodemax=[]):
    sum = tree.data
    for ch in tree.children:
        sum = sum + ch.data
    
    for child in tree.children:
        nodemax,summax = maxSumNode(child,summax,nodemax)
    if sum>summax:
        summax = sum
        nodemax = tree
    return nodemax,summax

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)