from Linkedlist import LinkedList
def nthToLast(ll,n):
    pointer1=ll.head
    pointer2=ll.head
    for i in range(n):
        if pointer2==None:
            return None
        pointer2=pointer2.next
    while pointer2:
        pointer2=pointer2.next
        pointer1=pointer1.next
    return pointer1.value
customLL=LinkedList()
customLL.generate(10,1,10)

print(customLL)
print(nthToLast(customLL,5))