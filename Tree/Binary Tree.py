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
inOrderTraversal(newBTreeNode)
