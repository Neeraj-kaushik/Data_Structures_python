def pairSum0(l):
    d={}
    for w in l:
        if -w in d:
            a=d[-w]
            for j in range(a):
                if w<-w:
                    print(w,-w)
                else:
                    print(-w,w)
        d[w]=d.get(w,0)+1
#Implement Your Code Here


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)