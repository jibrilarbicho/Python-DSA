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