def maxFreq(l):
    d = dict()
    for i in l:
        if i in d:
            d[i] = d.get(i, 0) + 1
        else:
            d[i] = 1
    max = -1
    for x in l:
        if d[x] > max:
            max = d[x]
            num = x        
            
    return num

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))