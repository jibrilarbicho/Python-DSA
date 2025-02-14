class Node:
    def __init__(self, value=None,next=None):
        self.value = value
        self.next = next
class Stack():
    def __init__(self):
        self.head = None
        self.minimumNode=None
    def min(self):
        if self.minimumNode is None:
            return None
        else:
            return self.minimumNode.value

    def push(self, value):
        if not self.minimumNode or (value<self.minimumNode.value):
            self.minimumNode=Node(value=value,next=self.minimumNode)
        
        self.head=Node(value=value,next=self.head)
    def pop(self):
        if self.head is None:
            return None
        else:
            self.minimumNode=self.minimumNode.next
            value=self.head.value
            self.head=self.head.next
            return value
    def minnOdes(self):
            while self.minimumNode.next!=None:
                print("min",self.minimumNode.value)
                self.minimumNode=self.minimumNode.next
            print("min",self.minimumNode.value)

            
stack=Stack()
stack.push(5)
stack.push(-200)
stack.push(8)

print("Minimum element is", stack.min())
stack.minnOdes()
