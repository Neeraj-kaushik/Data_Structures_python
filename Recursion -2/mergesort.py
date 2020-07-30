def merge(s1,s2,arr):
    i=0
    j=0
    k=0
    while i<len(s1) and j<len(s2):
        if s1[i]<s2[j]:
            arr[k]=s1[i]
            k+=1
            i+=1
        else:
            arr[k]=s2[j]
            k+=1
            j+=1
    while i<len(s1):
        arr[k]=s1[i]
        k+=1
        i+=1
    while j<len(s2):
        arr[k]=s2[j]
        k+=1
        j+=1


def mergesort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid =len(arr)//2
    s1=arr[0:mid]
    s2=arr[mid:]
    mergesort(s1)
    mergesort(s2)
    merge(s1,s2,arr)


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergesort(arr)
print(*arr)