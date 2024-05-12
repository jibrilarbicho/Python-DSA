class Stack:
    def __init__(self,maxsize):
        self.maxlenght=maxsize
        self.list = []
    def __str__(self) :
        self.list.reverse()
        value=[str(x) for x in self.list ]
        # reversed_list = list(reversed(self.list))  # Reverse the list
        # value = [str(x) for x in reversed_list]  
        return ' \n'.join(value)
    def IsEmpty(self) :
        if self.list==[] : 
            return True
        else :
            return False
    
    def pop(self) :
        if self.list==[] :
            return "The stack is empty"
        else :
            return self.list.pop()
        
    def peek(self) :
        if self.list==[] :
            return "The stack is empty"
        else :
            return self.list[len(self.list)-1]
    def isFull(self):
        if len(self.list)>=self.maxlenght:
            return True
        else :
            return False
    def push(self, value) :
        if self.isFull():
            return "The stack is full"
        else:
          self.list.append(value)
          return "The element has been successfuly pushed"
    def delete(self):
        self.list=[]
        

customStack=Stack(4)
customStack.push(1)

print(customStack.IsEmpty())
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.push(5))
print(customStack)
customStack.delete()
print(customStack)

# print(customStack.pop())
# print(customStack)
# print(customStack.peek())

