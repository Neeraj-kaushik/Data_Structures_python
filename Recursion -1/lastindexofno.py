## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(arr, x):
    l=len(arr)
    if l == 0:
        return -1
    
    a=arr[1:]
    smalla=lastIndex(a,x)
    if smalla != -1:
        return smalla + 1
    else:
        if arr[0]==x:
            return 0
        else:
            return -1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x))