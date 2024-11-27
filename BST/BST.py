class BST:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
    def insertNode(self,rootNode,node):
        if rootNode.data==None:
            rootNode.data=node
        elif rootNode.data<node:
            if rootNode.rightChild is None:
                rootNode.rightChild=BST(node)
            else:
                self.insertNode(rootNode.rightChild,node)
        else:
            if rootNode.leftChild is None:
                rootNode.leftChild=BST(node)
            else:
                self.insertNode(rootNode.leftChild,node)
        return "A node Succesfully inserted"
nebst=BST(1)
nebst.insertNode(nebst,2)
nebst.insertNode(nebst,3)
nebst.insertNode(nebst,4)
nebst.insertNode(nebst,5)
print(nebst.insertNode(nebst,6))