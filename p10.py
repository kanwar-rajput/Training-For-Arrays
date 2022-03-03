def getLengthOfArray(list):
    """
        Returns the length of Array
    """
    len = 0
    for _ in list:
        len += 1
    return len

def insertInMiddleElementOfArray(list,value):
    """
        Inserts at the middle element of Array
    """
    mid = getLengthOfArray(list)//2
    templist = []
    for i,j in enumerate(list):
        if i == mid:
            templist.append(value)
        templist.append(j)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
mid = insertInMiddleElementOfArray(l1,5)

# Printing
print(f"Inserted At the Middle : {mid}") # [1,2,5,3,4]