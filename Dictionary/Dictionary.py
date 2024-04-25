eng_sp_list = [("one", "uno"), ("two", "dos"), ("three", "tres")]
eng_sp_dict=dict(eng_sp_list)
print(eng_sp_dict)
newdict={}.fromkeys([1,2,3,4,5],2)
print(newdict)
myDict={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}
print(1 in myDict)
print("five" in myDict.values()) # to check values in dictionary