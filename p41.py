def sortArray(list , reverse = False):
    """
        Sorts Array Asecending/Decending
    """
    templist = []
    if reverse:
        while list:
            min = list[0]
            for x in list: 
                if x > min:
                    min = x
            templist.append(min)
            list.remove(min) 
    else:
        while list:
            min = list[0]
            for x in list: 
                if x < min:
                    min = x
            templist.append(min)
            list.remove(min) 
    return templist

# Array
l1 = [1,3,2,5,4]

# Before Sorting
print("Before Sorting : {l1}")

# Sorting i.e calling function
l1 = sortArray(l1)

# After Sorting
print("After Sorting : {l1}")