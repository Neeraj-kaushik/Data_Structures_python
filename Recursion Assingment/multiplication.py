def multiplication(m,n):
    if m==0 or n==0:
        return 0
    if n==1:
        return m
    else:
        return (m+multiplication(m,n-1))

m=int(input())
n=int(input())
a=multiplication(m,n)
print(a)
    