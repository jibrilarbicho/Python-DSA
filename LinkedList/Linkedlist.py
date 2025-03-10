from random import randint
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        # return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        # return self
    
# customll=LinkedList()
# customll.generate(10,1,100)
# print(customll)