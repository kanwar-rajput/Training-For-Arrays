def commonElementsOfArray(list1 , list2):
    """
        Returns Common Elements of Array
    """
    templist = []

    if len(list1) > len(list2):
        for i in list1:
            if i in list2:
                templist.append(i)
    else:
        for i in list2:
            if i in list1:
                templist.append(i)

    return templist


# Arrays
l1 = [1,2,3,4]
l2 = [4,5,6,7]

# Calling Function
l3 = commonElementsOfArray(l1,l2)

# Common Elements
print(f"Common Elements : {l3}") # [4]