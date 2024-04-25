class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
     temp_node = self.head
     result = ""
     while temp_node is not None:
         result += str(temp_node.value)
         if temp_node.next is not None:
             result += " =>"
         temp_node = temp_node.next
     return result
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
    def prepend(self, value):
       new_node = Node(value)
       if self.head is None:
           self.head = new_node
           self.tail = new_node
       else:
           new_node.next = self.head
           self.head = new_node
       self.length += 1
    def insert(self,index,value):
        newNode=Node(value)
        if index < 0 or index > self.length:
          print("Index out of range")
          exit(0)

        elif self.length==0:
            self.head=newNode
            self.tail=newNode

        elif index==0:
            newNode.next = self.head
            self.head=newNode
        else:
            tempNode=self.head

            for i in range(index-1):
               tempNode=tempNode.next
            newNode.next = tempNode.next
            tempNode.next=newNode
        
        self.length +=1







    


    
      
newLinkedlist=LinkedList()
newLinkedlist.append(1)
newLinkedlist.append(2)
newLinkedlist.append(3)
newLinkedlist.append(4)
newLinkedlist.append(5)
newLinkedlist.append(6)
newLinkedlist.prepend(7)
newLinkedlist.prepend(8)
newLinkedlist.prepend(9)
newLinkedlist.prepend(10)
newLinkedlist.insert(111,500)
print(newLinkedlist)