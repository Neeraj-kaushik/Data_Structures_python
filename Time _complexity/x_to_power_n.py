def power(x, n):
    a = 0
    if n == 0:
        return 1
    a = power(x, n//2)
    if n % 2 == 0:
        return a*a 
    else:
        return x*a*a

from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))    