def factorial(f):
    if f==1:
        return 1
    x=f*factorial(f-1)
    return x

f=int(input())
a=factorial(f)
print(a)