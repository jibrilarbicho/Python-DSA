import array
my_array = array.array("i",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in my_array:
    print(i)
my_array.insert(2,50)
print(my_array)
my_array.reverse()
# print(my_array)  # This line is commented out
