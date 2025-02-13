class CircularQueue:
    def __init__(self, maxsize):
        # self.items=[None for _ in range(maxsize)]
        self.items = [None] * maxsize
        self.maxsize=maxsize
        self.start=0
        self.end=0

    def __str__(self):
        return self.items
    
    
    def isFull(self):
        if self.start+1==self.end:
            return True
        elif self.start==0 and self.end+1==self.maxsize:
            return True
        else:
            return False
    
        
        
queue=CircularQueue(10)
print(queue.items)

        
