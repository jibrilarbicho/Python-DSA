def bubbleSort(customList):
    for i in range(len(customList)):
        for j in range(len(customList)-1):
            if customList[j]>customList[j+1]:
                # temp=customList[j]
                # customList[j]=customList[j+1]
                # customList[j+1]=temp
                customList[j],customList[j+1]=customList[j+1],customList[j]
    return customList
def selectSort(customList):
    for i in range(len(customList)):
        minindex=i
        for j in range (i+1,len(customList)):
            if customList[j]<customList[minindex]:
                minindex=j
        customList[i],customList[minindex]=customList[minindex],customList[i]
    return customList
def insertSort(CustomList):
    for i in range(1,len(CustomList)):
        key=CustomList[i]
        j=i-1
        while j>=0 and key<CustomList[j]:
            CustomList[j+1]=CustomList[j]
            j-=1
        CustomList[j+1]=key
        
    return CustomList

cList=[2,1,7,6,5,3,4,9,8]
print("bubbleSort",bubbleSort(cList))
print("selectSort",selectSort(cList))
print("insertSort",insertSort([8, 4, 6, 2, 9]))
                 
