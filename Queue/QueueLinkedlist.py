class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self) :
        return str(self.value)
class LinkedList:
        def __init__(self):
            self.head=None
            self.tail=None
        def __iter__(self):
             curNode=self.head
             while curNode:
                 yield curNode
                 curNode=curNode.next

class Queue:
     def __init__(self) :
          self.linkedlist=LinkedList()
     def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return ' -> '.join(values)
     
     def enqueue(self, value):
        newNode = Node(value)  # O(1)
        if self.linkedlist.head is None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode  # O(1)
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode  # O(1)



customQueue=Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)