def reverseStack(s1,s2):
    if len(s1) == 0 or len(s1) == 1:
        return 
    
    x = s1[-1]
    s1.pop()
    
    reverseStack(s1, s2)
    while len(s1) > 0:
        s2.append(s1[-1])
        s1.pop()
    
    s1.append(x)
    
    while len(s2) > 0:
        s1.append(s2[-1])
        s2.pop()
    
    return s1

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1,s2)
while(len(s1) !=0):
    print(s1.pop(),end= ' ')