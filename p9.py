def insertInEndOfArray(list,value):
    """
        Inserts a value at the end of the array
    """
    templist = []
    for i in list:
        templist.append(i)
    templist.append(value)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
l1 = insertInEndOfArray(l1,5)

# Printing
print(f"Inserted At the End : {l1}") # [1,2,3,4,5]