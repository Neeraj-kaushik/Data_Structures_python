def count_zero(a):
    if a==0:
        return 0
    c=0
    if a%10==0:
        return 1+count_zero(int(a/10))
    else:
        return count_zero(int(a/10))

a=int(input())
x=count_zero(a)
print(x)