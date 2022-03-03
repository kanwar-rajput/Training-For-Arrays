def insertAtIndexInc(list , value, index):
    """
        Inserts a value at Specific Index + 1
    """
    templist = []
    for index_,value_ in enumerate(list):
        if index_ == index+1:
            templist.append(value)
        templist.append(value_)
    return templist

# Array
l1 = [1,2,3,4]

# Calling Function
l1 = insertAtIndexInc(list = l1 , value = 5, index=2)

# Printing
print(l1)