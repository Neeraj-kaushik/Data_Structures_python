class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def ll():
    linkedlist=[int(a) for a in input().split()]
    head =None
    tail=None
    for data in linkedlist:
        if data== -1:
            break
        newnode=Node(data)
        if head is None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=newnode
    return head
def count(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count

def delete(head,i):
    if i<0 or i>count(head):
        return head
    if i==0:
        head=head.next
    else:
        curr=head
        for j in range(0,i-1):
            curr=curr.next
        end=curr.next.next
        curr.next=None
        curr.next=end
    return head
        
def printll(head):
    while head is not None:
        print(str(head.data),end=" ")
        head=head.next
    return

t=int(input())
while t>0:
    head=ll()
    i=int(input())
    head=delete(head,i)
    printll(head)
    t=t-1