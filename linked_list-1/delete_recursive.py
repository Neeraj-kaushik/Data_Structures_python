class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    if head == None:
        return None
    if i < 0:
        return head
    if i == 0 :
        return head.next
    
    
    dele = deleteRec(head.next, i-1)
    head.next = dele
    
    return head    
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


from sys import setrecursionlimit
setrecursionlimit(11000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i=int(input())
l = deleteRec(l, i)
printll(l)

