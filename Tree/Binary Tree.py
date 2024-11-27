import sys
sys.path.append("/mnt/c9542373-6611-4b24-a6c7-2979563b4e53/Documents/Python-DSA/Queue")
from QueueLinkedlist import Queue

class TreeNode:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None
def preOrderTraversal(rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)
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
     while not customQueue.isEmpty():
          root=customQueue.dequeue()
          print(root.data)
          if not root.left is None:
               customQueue.enqueue(root.left)
          if not root.right is None:
               customQueue.enqueue(root.right)


  
    
newBTreeNode = TreeNode("Drinks")
Leftchild=TreeNode("Hot")
tea=TreeNode("tea")
coffe=TreeNode("coffe")
Leftchild.left=tea
Leftchild.right=coffe
Rightchild=TreeNode("Cold")

newBTreeNode.left=Leftchild
newBTreeNode.right=Rightchild
# preOrderTraversal(newBTreeNode)
# inOrderTraversal(newBTreeNode)
LevelOrderTraversal(newBTreeNode)
