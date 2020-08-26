import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647
def findMax(root): 
       
    if (root == None):  
        return INT_MIN
    res = root.data 
    lres = findMax(root.left)  
    rres = findMax(root.right)  
    if (lres > res): 
        res = lres  
    if (rres > res):  
        res = rres  
    return res 

def findMin(root):  
    if (root == None):  
        return INT_MAX
  
    res = root.data 
    lres = findMin(root.left)  
    rres = findMin(root.right)  
    if (lres < res): 
        res = lres  
    if (rres < res):  
        res = rres  
        
    return res 


def minMax(root):
    min = findMin(root)
    max = findMax(root)
    
    return min, max

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
minimum, maximum = minMax(root)
print(maximum, minimum)