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

def printIthNode(head,i):
    count=0
    while head is not None:
        if count==i:
            return head
        head=head.next
        count+=1
        


t=int(input())
while t>0:
    head=ll()
    i=int(input())
    node=printIthNode(head, i)
    if node:
        print(node.data)
    t=t-1