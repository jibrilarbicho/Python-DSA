from Linkedlist import LinkedList
def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head
    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()
customLL.generate(10, 0, 99)
print("Original List:")
print(customLL)

x = 50
partition(customLL, x)
print("Partitioned List with partition value", x, ":")
print(customLL)
