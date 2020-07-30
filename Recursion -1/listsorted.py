def listsorted(arr,si):
    l=len(arr)
    if si==l-1 or si==1:
        return True
    if arr[si]>arr[si+1]:
        return False
    newlistsorted=listsorted(arr,si+1)
    return newlistsorted
    

n =int(input())
arr= list(int(x) for x in input().split())
si=int(input())
listsorted(arr,si)
if listsorted(arr,si):
    print("true")
else:
    print("false")
