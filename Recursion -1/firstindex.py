def firstIndex(arr, x):
    l=len(arr)
    if l==0:
        return -1
    if arr[0]==x:
        return 0
    a=arr[1:]
    smalla=firstIndex(a,x)
    if smalla==-1:
        return -1
    else:
        return smalla+1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))