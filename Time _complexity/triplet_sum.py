
n = int(input())
list = [int(x) for x in input().split()]
list.sort()
 
r = int(input())
for j in range(n):
    st=j+1
    end=n-1              
    m=r-list[j]
    while st<=end and end<n and st>-1:
        if list[st]+list[end]>m:
            end-=1
        elif list[st]+list[end]<m:
            st+=1
        else:
            c1=0
            c2=0
            for i in range(st,end+1):
                if list[st]==list[i]:
                    c1=c1+1
                else:
                    break
            for i in range(end,st-1,-1):
                if list[end]==list[i]:
                    c2=c2+1
                else:
                    break
            if list[st]==list[end]:
                com=((end-st+1)*(end-st))//2
            else:
                com=c1*c2
            for i in range(com):
                print(str(list[j]),str(list[st]),str(list[end]))
            st=st+c1
            end=end-c2