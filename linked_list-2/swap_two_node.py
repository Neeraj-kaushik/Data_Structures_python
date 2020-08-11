class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def swap_nodes(head, i, j):
  if ((i == 0 or j == 0) and (abs(i-j) == 1)): 

      curr1 = head
      head = head.next
      adv1 = head.next
      head.next = curr1
      curr1.next = adv1

  elif i == 0 or j == 0:
    if i == 0:
      curr1 = head
      ptr2 = head
      cnt = 1

      while cnt < j:
        cnt += 1
        ptr2 = ptr2.next

      curr2 = ptr2.next
       
      adv1 = curr1.next
      adv2 = curr2.next

      head = curr2
      curr2.next = adv1
      ptr2.next = curr1
      curr1.next = adv2

    elif j == 0:
      curr2 = head
      ptr1 = head
      cnt = 1

      while cnt < i:
        cnt += 1
        ptr1 = ptr1.next

      curr1 = ptr1.next
       
      adv2 = curr2.next
      adv1 = curr1.next

      head = curr1
      curr1.next = adv2
      ptr1.next = curr2
      curr2.next = adv1
    
  
  elif abs(i-j) == 1:
    if i < j:     
      cnt1 = 1
      cnt2 = 1
      ptr1 = head
      ptr2 = head

      while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
      curr1 = ptr1.next
      adv1 = curr1.next

      while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
      curr2 = ptr2.next
      adv2 = curr2.next
      
      ptr1.next = curr2
      curr2.next = curr1
      curr1.next = adv2

    elif j < i:     
      cnt1 = 1
      cnt2 = 1
      ptr1 = head
      ptr2 = head

      while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
      curr2 = ptr2.next
      adv2 = curr2.next

      while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
      curr1 = ptr1.next
      adv1 = curr1.next
      
      ptr2.next = curr1
      curr1.next = curr2
      curr2.next = adv1
  
  else:
      cnt1, cnt2 = 1,1
      ptr1, ptr2 = head, head
      while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
      curr2 = ptr2.next
      adv2 = curr2.next

      while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
      curr1 = ptr1.next
      adv1 = curr1.next

      ptr1.next = curr2
      curr2.next = adv1
      ptr2.next = curr1
      curr1.next = adv2

  return head

def ll(arr):
  if len(arr) == 0:
    return None
  head = Node(arr[0])
  last = head
  for data in arr[1:]:
    last.next = Node(data)
    last = last.next

  return head
   
def printll(head):
  while head:
    print(head.data, end = " ")
    head = head.next
  print()

arr = list(int(x) for x in input().split())
l = ll(arr[:-1])
i, j = list(int(i) for i in input().split())
l = swap_nodes(l, i, j)