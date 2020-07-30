def sum_of_digit(a):
    if a==0:
        return 0
    return (a%10+sum_of_digit(int(a/10)))

a=int(input())
x=sum_of_digit(a)
print(x)