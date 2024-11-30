import sys
sys.path.append("/mnt/c9542373-6611-4b24-a6c7-2979563b4e53/Documents/Python-DSA/Queue")
from QueueLinkedlist import Queue
class AVL():
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1
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
