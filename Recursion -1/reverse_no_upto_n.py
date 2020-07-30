def number(n):
    if n==0:
        return n
    print(n) 
    number(n-1)
    

n=int(input())
x=number(n)
print(x)