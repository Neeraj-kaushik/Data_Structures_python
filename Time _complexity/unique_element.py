def FindUnique(arr):
    unique = arr[0]
    for i in range(1, len(arr)):
      unique = unique ^ arr[i]
      
    return unique
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
