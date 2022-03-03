def doesExist(list,element): # Pythonic
    """
        Tells whether an element is in Array
    """
    return element in list

def doesExist2(list,element):
    """
        Tells whether an element is in Array
    """

    status = 0
    for i in list:
        if i == element:
            status += 1

        if (status != 0):
            return True
        else:
            return False

# Array
l1 = [1,2,3,4]

# Checking Elements
print(doesExist(l1,5)) # False
print(doesExist2(l1,1)) # True
