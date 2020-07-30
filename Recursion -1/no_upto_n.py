def number(n):
    if n==0:
        return n
    number(n-1)
    print(n) 

n=int(input())
x=number(n)
print(x)