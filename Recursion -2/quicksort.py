def partition(arr,start,end):
    a =arr[start]
    c=0
    for i in range(start,end+1):
        if arr[i] < a:
            c=c+1
    arr[start+c],arr[start]=arr[start],arr[start+c]
    p=start+c
    i=start
    j=end
    while i<j:
        if arr[i] <a:
            i=i+1
        elif arr[j]>a:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
    return p


def quickSort(arr, start, end):
    if start>end:
        return
    p=partition(arr,start,end)
    quickSort(arr,start,p-1)
    quickSort(arr,p+1,end)


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n)
print(*arr)