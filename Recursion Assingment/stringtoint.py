def stringtointeger(str1):
    if len(str1)==1:
        return ord(str1[0])-ord('0')
    
    a=stringtointeger(str1[1:])
    a1=ord(str1[0])-ord('0')
    a1=a1*(10**(len(str1)-1))+a
    return int(a1)

str1=str(input())
print(stringtointeger(str1))