class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack():
    def __init__(self):
        self.head = None
        self.minimum=None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.minimum = self.head

        else:
            if value < self.minimum.value:

                self.minimum = new_node
            new_node.next = self.head
            self.head = new_node
stack=Stack()
stack.push(3)
stack.push(0)
stack.push(-200)
stack.push(1)
print("Minimum element is", stack.minimum.value)