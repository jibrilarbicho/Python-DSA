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

    
newBTreeNode = TreeNode("Drinks")
Leftchild=TreeNode("Hot")
Rightchild=TreeNode("Cold")
newBTreeNode.left=Leftchild
newBTreeNode.right=Rightchild
preOrderTraversal(newBTreeNode)
