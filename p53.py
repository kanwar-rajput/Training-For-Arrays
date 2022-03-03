def doesElementExist(list,element): # Pythonic
    """
        Returns the element of index in Array
    """
    return -1 if element not in list else list.index(element)

def doesElementExist2(list,element):
    """
        Returns the element of index in Array
    """
    index = 0
    for i in list:
        if i == element:
            return index
        index += 1
    return -1

# Array
l1 = [1,2,3,4]

# Calling Function
print(f"Found : {doesElementExist(l1,2)}")

# Calling Function 2
print(f"Found : {doesElementExist2(l1,5)}")