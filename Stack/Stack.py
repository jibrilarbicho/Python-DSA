class Stack:
    def __init__(self):
        self.list = []
    def __str__(self) :
        values=self.list.reverse()
        value=[str(x) for x in values ]
        return ' -> '.join(value)