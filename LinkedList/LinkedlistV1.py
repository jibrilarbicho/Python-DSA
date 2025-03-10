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
    def traverse(self):
        current=self.head
        emoji="🧑‍🦰"
        #        while current is not None:

        while current:
            print(f"{current.value} {emoji}")
            current=current.next
    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value==target:
                return f"it is found at index:{index}"
            current=current.next
            index+=1
        return False
    def  get(self,index):
        if index <0 or index>self.length:
            return "Out of index"
        else:
          current=self.head
          for _ in range(index):
             current=current.next
          return current
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def pop_first(self):
        if self.length==0:
            return "There is no elemnt in Linkedlist"
        popedNode=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
            return popedNode.value
        else :
            self.head=self.head.next
            popedNode.next=None
            self.length-=1
            return popedNode.value
    def pop(self):
            popedNode=self.tail
            if self.length==1:
                self.head=None
                self.tail=None
            else:


               temp=self.head

               while  temp.next is not self.tail:
                   temp=temp.next
               temp.next=None
               self.tail=temp
            self.length-=1
            return popedNode.value
    def remove(self,index):
        if index==0:
            return self.pop_first()
        else:
          prevNode=self.get(index-1)
          popedNode=prevNode.next
          prevNode.next=popedNode.next
          popedNode.next=None
          self.length-=1
          return popedNode.value
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0


    def find_middle(self):
      slow = self.head
      fast = self.head
      while fast is not None and fast.next is not None:
          slow = slow.next
          fast = fast.next.next
      return slow.value







    


    
      
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
newLinkedlist.insert(1,500)
print(newLinkedlist.pop_first())
print(newLinkedlist.pop())
print(newLinkedlist.remove(2))
# newLinkedlist.delete_all()


# newLinkedlist.traverse()
# print(newLinkedlist.search(6))
# print(newLinkedlist.get(-2))
print(newLinkedlist)
print(newLinkedlist.find_middle())

# newLinkedlist.set_value(2,456)
print(newLinkedlist)