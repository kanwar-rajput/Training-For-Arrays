def insertAtIndex(list , value, index):
    """
        Inserts a value at Specific Index
    """
    templist = []
    for index_,value_ in enumerate(list):
        if index_ == index:
            templist.append(value)
        templist.append(value_)
    return templist

# Array
l1 = [1,2,3,4]

# Calling Function
l1 = insertAtIndex(list = l1 , value = 5, index=2)

# Printing
print(l1)