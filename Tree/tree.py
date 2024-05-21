class TreeNode:
    def __init__(self, data, children=None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# Create the tree
tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])

tree.addChild(cold)
tree.addChild(hot)
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)
