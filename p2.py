def copyArray(list1):
    """
        Write a code that assign the values of an array into another array
    """
    templist = []
    for i in list1:
        templist.append(i)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4]
l2 = []

# Calling Function
l2 = copyArray(l1)

# Printing Array
print(f"Copied data of Array : {l2}") # [1, 2, 3, 4]