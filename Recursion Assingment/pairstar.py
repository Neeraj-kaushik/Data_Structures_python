def pairstar(str1,str2,i=0):
    str2=str2+str1[i]
    if i==len(str1)-1:
        print(str2)
        return
    
    if str1[i]==str1[i+1]:
        str2=str2+"*"
    pairstar(str1,str2,i+1)

str1=str(input())
str2=""
pairstar(str1,str2)