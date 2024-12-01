import math
def binaryserach(customList,value):
    start=0
    end=len(customList)-1
    middle=math.floor((end+start)/2)
    while start<=end:
        if customList[middle]==value:
            return f"the value is exist at index of {middle}"
        elif customList[middle]<value:
            start=middle+1
        else:
            end=middle-1
        middle=math.floor((end+start)/2)
    return "the value is not exist"
cList=[1,2,3,4,5,6,7,8,9]
print(binaryserach(cList,1))



            

