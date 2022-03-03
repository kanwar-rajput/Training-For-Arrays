def insertInStartOfArray(list,value):
    """
        Inserts a value at the start of the array
    """
    templist = []
    templist.append(value)
    for i in list:
        templist.append(i)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
l1 = insertInStartOfArray(l1,5)

# Printing
print(f"Inserted At the Start : {l1}") # [5,1,2,3,4]