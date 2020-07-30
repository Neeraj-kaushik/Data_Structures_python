def string_pallindrome(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return string_pallindrome(s[1:-1])
        else:
            return False
    
a=str(input())
if string_pallindrome(a):
    print("true")
else:
    print("false")