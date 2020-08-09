def pairSum(arr, x):
    for i in range(0, len(arr)-1):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == x:
                if arr[i] > arr[j]:
                    print(arr[j], arr[i])
                else:
                    print(arr[i], arr[j])
    
    
    
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)