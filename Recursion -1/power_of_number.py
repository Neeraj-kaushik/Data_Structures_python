def power_n(n,p):
    if p==0:
        return 1
    a=n*power_n(n,p-1)
    return a

str=input().split()
n,p=int(str[0]),int(str[1])
x=power_n(n,p)
print(x)