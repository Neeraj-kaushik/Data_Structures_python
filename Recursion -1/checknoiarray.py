def checkNumber(arr, x):
    l=len(arr)
    if l==0:
        return 0    
    if arr[0]==x:
        return True
    a=arr[1:]
    smalla=checkNumber(a,x)
    if smalla==-1:
        return False
    else:
        return True

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')