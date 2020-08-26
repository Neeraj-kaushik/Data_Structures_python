import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder):
    if len(preorder) == 0:
        return None
    rootData = preorder[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None
    
    leftInorder = inorder[0:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1:]
    
    lenLeftSubtree = len(leftInorder)

    leftPreorder = preorder[1:lenLeftSubtree + 1]
    rightPreorder = preorder[lenLeftSubtree + 1:]
    
    leftChild = buildTreePreOrder(leftPreorder, leftInorder)
    rightChild = buildTreePreOrder(rightPreorder, rightInorder)
    
    root.left = leftChild
    root.right = rightChild
    
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
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)