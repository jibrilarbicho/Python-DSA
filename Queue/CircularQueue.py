class CircularQueue:
    def __init__(self, maxsize):
        # self.items=[None for _ in range(maxsize)]
        self.items = [None] * maxsize
        self.maxsize=maxsize
        self.start=0
        self.end=0

    def __str__(self):
        return " ".join([str(x) for x in self.items])
    
    
    def isFull(self):
        if self.start==self.end+1:
            return True
        elif self.start==0 and self.end==self.maxsize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.end==0:
            return True
        else:
            return False
    def enqueue(self, item):
        if self.isFull():
            return "Queue is full"
        else:
            if self.end==self.maxsize:
                self.end=0
                
            else:
                self.items[self.end] = item
                print(self.items)
                self.end+=1
                return f"The elemnt is inserted {item} "
           
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            self.items[self.start]=None

        
            if self.start==self.maxsize:
                self.start=0
            else:
                self.start+=1
            
        






        


    
        
        
queue=CircularQueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)



queue.dequeue()
print(queue)

queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
print(queue.enqueue(4))
print(queue.enqueue(5))
print(queue)




# print(queue)
# print(queue.isFull())

# print(queue.items)

        
