# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    if head is None:
        return head
    curr = head
    
    head1 = None
    head2 = None
    
    while curr is not None:
        if curr.data &1:
            if head1 is None:
                head1 = curr
                tail1 = curr
            else:
                tail1.next = curr
                tail1 = tail1.next
        else:
            if head2 is None:
                head2 = curr
                tail2 = curr
            else:
                tail2.next = curr
                tail2 = tail2.next
                        
        curr = curr.next
        
    if head1 is None or head2 is None:     
        return head
    
    tail2.next = None        
    tail1.next = head2
        
    return head1

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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)