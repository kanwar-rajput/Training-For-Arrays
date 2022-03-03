def removeDuplicatesFromArray(list):
    """
        Removes Duplicate Elements from the Array
    """
    # We will use this Array to store unique values
    templist = []

    for i in list:
        if not i in templist:
            templist.append(i)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4,4,3,2]

# Before Removing Duplicates
print(f"Before Removing Duplicates : {l1}")

# Removing Duplicates
l1 = removeDuplicatesFromArray(l1)

# After Removing Duplicates
print(f"After Removing Duplicates  : {l1}")