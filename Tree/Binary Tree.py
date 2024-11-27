import sys
sys.path.append("/mnt/c9542373-6611-4b24-a6c7-2979563b4e53/Documents/Python-DSA/Queue")
from QueueLinkedlist import Queue
items=[]
class TreeNode:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None
def preOrderTraversal(rootNode):
        if not rootNode:
            return
     #    print(rootNode.data)
        items.append(rootNode.data)
        
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)
        return items
def inOrderTraversal(rootNode):
     if not rootNode:
          return
     inOrderTraversal(rootNode.left)
     print(rootNode.data)
     
     inOrderTraversal(rootNode.right)
def LevelOrderTraversal(rootNode):
     if not rootNode:
          return
     customQueue=Queue()
     customQueue.enqueue(rootNode)
     items.append(rootNode.data)
     while not customQueue.isEmpty():
          root=customQueue.dequeue()
          print(root.data)
          if not root.left is None:
               customQueue.enqueue(root.left)
          if not root.right is None:
               customQueue.enqueue(root.right)
     return items
def SearchBT(rootNode,value):
     if rootNode is None:
          return
     customQueue=Queue()
     customQueue.enqueue(rootNode)
     while not customQueue.isEmpty():
          root=customQueue.dequeue()
          if root.data==value:
               return "Sucess"
               
          if not root.left is None:
               customQueue.enqueue(root.left)
          if not root.right is None:
               customQueue.enqueue(root.right)

  
    
# newBTreeNode = TreeNode("Drinks")
# Leftchild=TreeNode("Hot")
# tea=TreeNode("tea")
# coffe=TreeNode("coffe")
# Leftchild.left=tea
# Leftchild.right=coffe
# Rightchild=TreeNode("Cold")

# newBTreeNode.left=Leftchild
# newBTreeNode.right=Rightchild
# inOrderTraversal(newBTreeNode)
# LevelOrderTraversal(newBTreeNode)
def Insertion(newBTreeNode,rootNode,child,side):

     if rootNode is None:
          return
     customQueue=Queue()
     customQueue.enqueue(newBTreeNode)
     while not customQueue.isEmpty():
          root=customQueue.dequeue()
          print("queue",root,rootNode)
          if str(root.data)==str(rootNode):
               if side=="R":
                    root.right=child
                    print(f"Element {child.data} inserted as the right child of {rootNode} {LevelOrderTraversal(newBTreeNode)} ")
               elif side=="L":
                    root.left=child
                    print(f"Element {child.data} inserted as the left child of {rootNode} {LevelOrderTraversal(newBTreeNode)} ")
               
               return 
          if not root.left is None:
               customQueue.enqueue(root.left)
          if not root.right is None:
               customQueue.enqueue(root.right)



def main():
     newBTreeNode = TreeNode("Drinks")
     Leftchild=TreeNode("Hot")
     tea=TreeNode("tea")
     coffe=TreeNode("coffe")
     Leftchild.left=tea
     Leftchild.right=coffe
     Rightchild=TreeNode("Cold")

     newBTreeNode.left=Leftchild
     newBTreeNode.right=Rightchild
     preOrderTraversal(newBTreeNode)
     parentNode=input(f"Choose a parent Node from {items}:")
     if parentNode not in items:
          print("Please select correct parent node")
          return
     else:
          child=input("Enter the child node value:")
          side=input(f"Enter the side R for right child of parent and L for Left side of parent Node({parentNode}):")
          child=TreeNode(child)

          Insertion(newBTreeNode,parentNode,child,side)
main()