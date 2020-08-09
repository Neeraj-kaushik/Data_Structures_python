def equilibriumIndex(arr):
  sum1 = sum(arr)             
  prev = 0                    
  next = 0
  for i in range(0, len(arr)-1):
    prev += arr[i]
    next = sum1 - prev - arr[i+1]
    if prev == next:
      return i+1
  
  return -1

n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))