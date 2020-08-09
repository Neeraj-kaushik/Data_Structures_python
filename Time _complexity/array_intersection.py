def binary(arr, l, h, key):
  mid = (l+h)// 2

  if l > h:
    return -1

  if arr[mid] == key:
    return mid
  
  if key < arr[mid]:
    return binary(arr, l, mid-1, key)
  else:
    return binary(arr, mid+1, h, key)  

def intersection(arr1, arr2):
  if len(arr1) < len(arr2):
    arr1.sort()
    p2 = 0
    l2 = len(arr2)

    while l2 > 0:
      if binary(arr1, 0, len(arr1)-1, arr2[p2]) != -1:
        print(arr2[p2])   
      p2 += 1
      l2 -= 1

  else:
    arr2.sort()
    p1 = 0
    l1 = len(arr1)
    while l1 > 0:
      if binary(arr2, 0, len(arr2)-1, arr1[p1]) != -1:
        print(arr1[p1])   
      p1 += 1
      l1 -= 1 
  
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' ')[:n1])

n2=int(input())
arr2=list(int(i) for i in input().strip().split(' ')[:n2])

intersection(arr1, arr2)
