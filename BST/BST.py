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
    def searchInBST(self,rootNode,node):
        if rootNode.data is None: return
        elif rootNode.data==node: 
             print("node is found and it is root Node") 
             return
        elif rootNode.data>node:
            if rootNode.leftChild.data==node:
                print( f"Node is found in the left child of {rootNode.data}")
                return
            else:
                self.searchInBST(rootNode.leftChild,node)
        elif rootNode.data<node:
            if rootNode.rightChild.data==node:
                print(f"Node is found in the right child of {rootNode.data}")
                return
            else:
                self.searchInBST(rootNode.rightChild,node)
        else:
            print("Node not found")
            return


def minValue(bstNode):
    if bstNode.data==None: return
    while bstNode.leftChild is not None:
        bstNode=bstNode.leftChild
    return bstNode.data    
nebst=BST(1)
nebst.insertNode(nebst,2)
nebst.insertNode(nebst,3)
nebst.insertNode(nebst,4)
nebst.insertNode(nebst,5)
print(nebst.insertNode(nebst,6))
nebst.searchInBST(nebst,4)