
def checkBalanced(exp):
    arr=[]
    for char in exp:
        if char in '({[':
            arr.append(char)
        elif char is ')':
            if (not arr or arr[-1]!='('):
                return False
            arr.pop()
        elif char is '}':
            if (not arr or arr[-1]!='{'):
                return False
            arr.pop()
        elif char is ']':
            if (not arr or arr[-1]!='['):
                return False
            arr.pop()
    if (not arr):
        return True
    return False


exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')
