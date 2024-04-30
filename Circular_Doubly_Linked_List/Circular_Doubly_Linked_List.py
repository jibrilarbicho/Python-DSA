class Node:
    def __init__(self,value) :
        self.value=value
        self.prev=None
        self.next=None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
       node = self.head
       while node:
           yield node
           node = node.next
        #    if node==self.head:
        #       break
           if node==self.tail.next:
              break
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "CDLL is created successfully"
    def insertNode(self, nodeValue, location):
       if self.head is None:
        print("The node cannot be inserted")
       else:
        newNode = Node (nodeValue)
       if location == 0:
         newNode.prev = None
         newNode.next = self.head
         self.head.prev = newNode
         self.head = newNode
       elif location == 1:
          newNode.next = None
          newNode.prev = self.tail
          self.tail.next = newNode
          self.tail = newNode
       else:
        tempNode = self.head
        index = 0
        while index < location - 1:

         tempNode = tempNode.next
         index += 1
        newNode.next = tempNode.next
        newNode.prev = tempNode
        newNode.next.prev = newNode
        tempNode.next = newNode
     


circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
print([node.value for node in circularDLL])

