class Node:
    def __init__(self,value=None) :
      self.value = value
      self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __iter__(self):
       node = self.head
       while node:
           yield node
           if node.next == self.head:
              break
           node = node.next
    def create(self,NodeValue):
       node=Node(NodeValue)
       node.next=node
       self.head=node
       self.tail=node
    def insert(self,location,nodeValue):
        if self.head is None:
          return "The head refernce is None"
        else:
          node=Node(nodeValue)
          if location==0:
           node.next=self.head
           self.head=node

           self.tail.next=node
          elif location==1:
             node.next=self.tail.next
             self.tail.next=node
             self.tail=node
          else:
            tempNode=self.head
            index=0
            while index<location-1:
                 tempNode=tempNode.next
                 index+=1
            nextNode=tempNode.next
            tempNode.next=node
            node.next=nextNode
          return "The node has been successfullly created"


    def traverseCLL(self):
       if self.head is None: 
          print("There is no any elemenet for traversal")
       tempnode=self.head
      #  while tempnode.next is not self.head:
      #     print(tempnode.value)
         
      #     tempnode=tempnode.next
      #  print(tempnode.value)
       while tempnode:
          print(tempnode.value)
          tempnode=tempnode.next
          if tempnode==self.head:
             break
          


       

       


circularSSL=LinkedList()
print(circularSSL.create(1))
circularSSL.insert(0,0)
circularSSL.insert(2,1)
circularSSL.insert(3,1)
circularSSL.insert(2,2)


print([node.value for node  in circularSSL])
circularSSL.traverseCLL()