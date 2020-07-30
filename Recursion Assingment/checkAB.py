def checkAB(str1):
    if len(str1) == 0:
        return True
    if len(str1) == 1:
        if str1 == 'a':
            return True
        else:
            return False
    if str1[0] == 'a':
        return checkAB(str1[1:])
    elif str1[0] == 'b':
        if str1[1] == 'b':
            return checkAB(str1[2:])
        else:
            return False
    else:
        return False

str1=str(input())
a=checkAB(str1)
if a==True:
    print('true')
else:
    print('false')