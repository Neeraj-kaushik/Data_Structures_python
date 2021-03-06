import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if len(postorder) == 0:
        return None
    
    rootData = postorder[len(postorder) - 1]
    root = BinaryTreeNode(rootData)
    rootIndex = -1
    
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndex = i
            break
    if rootIndex == -1:
        return None
    
    leftInorder = inorder[:rootIndex]
    rightInorder = inorder[rootIndex + 1:]
    
    x = len(leftInorder)    
    leftPostorder = postorder[:x]
    rightPostorder = postorder[x:len(postorder) - 1]
    
    root.left = buildTreePostOrder(leftPostorder, leftInorder)    # Where to call recursion?
    root.right = buildTreePostOrder(rightPostorder, rightInorder)
    
    return root

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)