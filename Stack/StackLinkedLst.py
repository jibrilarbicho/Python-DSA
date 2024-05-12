class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return'-> '.join(values)
    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    def push(self,value):
        node=Node(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue
customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print(customStack.pop())
print(customStack)