class Heap:
    def __init__(self,size):
        self.heapSize = 0
        self.customList=(size+1)*[None]
        self.maxSize=size+1
def peakOfHeap(rootNode):
        if not rootNode:
            return
        return rootNode.customList[1]
def sizeOfHeap(rootNode):
        if not rootNode:
            return
        return rootNode.heapSize
def levelOrderTraversal(rootNode):
        if not rootNode:
            return
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])
def heapifyTree(rootNode,index,heaptype):
        parentIndex=int(index/2)
        if index<=1:
            return
        if heaptype=="Min":
            if rootNode.customList[index]<rootNode.customList[parentIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[parentIndex]
                rootNode.customList[parentIndex]=temp
                heapifyTree(rootNode,parentIndex,heaptype)
        elif heaptype=="Max":
            if rootNode.customList[index]>rootNode.customList[parentIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[parentIndex]
                rootNode.customList[parentIndex]=temp
                heapifyTree(rootNode,parentIndex,heaptype)
def insertNode(rootNode,nodeValue,heaptype):
        if rootNode.heapSize+1==rootNode.maxSize:
            return "Heap is full"
        rootNode.customList[rootNode.heapSize+1]=nodeValue
        rootNode.heapSize+=1
        heapifyTree(rootNode,rootNode.heapSize,heaptype)
        return "Value inserted successfully"
    

newbinaryHeap=Heap(5)
insertNode(newbinaryHeap,4,"Max")
insertNode(newbinaryHeap,5,"Max")
insertNode(newbinaryHeap,2,"Max")
insertNode(newbinaryHeap,1,"Max")
levelOrderTraversal(newbinaryHeap)
