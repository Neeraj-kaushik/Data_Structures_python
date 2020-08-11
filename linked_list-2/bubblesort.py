class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubbleSortLL(head) :
   
    end = None
    while end != head:
        p = head
        while p.next != end:
            q = p.next
            if p.data > q.data:
                p.data, q.data = q.data, p.data
            p = p.next
        end = p

    return end           
        
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
        
    return head
    
def printll(head):
    while head:
        print(head.data, end = " ")
        head = head.next
    print()
    
arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = bubbleSortLL(l)