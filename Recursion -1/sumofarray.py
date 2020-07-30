def sumofarray(arr):
    if len(arr)==0:
        return 0
    else :
        return arr[0]+sumofarray(arr[1:])
    

n =int (input())
arr=list(int(x) for x in input().split())
print(sumofarray(arr))
