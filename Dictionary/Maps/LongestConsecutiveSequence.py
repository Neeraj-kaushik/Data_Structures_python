class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        
    def size():
        return self.count
    
    def getBucketIndex(self, hc):
        return (abs(hc) % (self.bucketSize))
    
    def rehash(self):
        temp = self.buckets
        self.bucketSize *= 2
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next
    
    def search(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def remove(self, key):
        hc = hash(key)
        index = getBucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev == None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next                
                self.count -= 1
                return head.value
            prev = head            
            head = head.next
            
        return None    
        
    
    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()
        
def longestConsecutiveSubsequence(arr):
    m = Map()
    for i in arr:
        m.insert(i, True)
    
    maxCount = -10
    maxStart = -10
   
    for i in arr:
        
        start = i
        j = i+1
        count = 1
        flag = True
        
        while flag:
            if m.search(j) is True:
                count += 1
                m.insert(j, False)
                j = j + 1              
            else:
                flag = False
            
        j = i - 1                           
        flag = True
        while flag:
            if m.search(j) is True:            
                start = j
                m.insert(j, False)
                j = j - 1
                count += 1                
            else:
                flag = False
              
        if maxCount < count:
            maxCount = count
            maxStart = start
            
        elif maxCount == count:
            if arr.index(maxStart) > arr.index(start):               
                maxStart = start      
            
    return maxCount, maxStart
        

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))

length, start = longestConsecutiveSubsequence(arr)
for i in range(0, length, 1):
    print(start+i)