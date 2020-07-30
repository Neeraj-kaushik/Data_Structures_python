def gsum(k):
    if k==0:
        return 1
    x=1/pow(2,k)+gsum(k-1)
    return x

k=int(input())
a=gsum(k)
print(a)