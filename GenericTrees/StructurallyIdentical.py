import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
   
    q1=queue.Queue()
    q2=queue.Queue()
    q1.put(tree1)
    q2.put(tree2)
    while (not(q1.empty() or q2.empty())):
        c1=q1.get()
        c2=q2.get()
        if c1.data!=c2.data:
            return False
        for child in c1.children:
            q1.put(child)
        for child in c2.children:
            q2.put(child)
    return True  

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
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')