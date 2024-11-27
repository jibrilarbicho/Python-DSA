import array
my_array = array.array("i",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# for i in my_array:
#     print(i)
my_array.insert(2,50)
# print(my_array)
# my_array.reverse()
# print(my_array)  # This line is commented out
#Accessing an element of Array
def AccessElement(array,index):
    if index>len(array):
        print("Index out of range")
    else:
        print(array[index])
AccessElement(my_array,2)
def LinearSearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
print(LinearSearch(my_array,3))
#Remove last Array element by pop method
my_array.pop()
print(my_array)
print(my_array.tolist())
import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 2, 3)
