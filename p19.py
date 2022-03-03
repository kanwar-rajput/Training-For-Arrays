def getEvenElementsOfArray(list):
    """
        Returns the Even Elements of Array
    """
    templist = []
    for i in list:
        if (i%2==0):
            templist.append(i)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Making empty list for storing evens
evens = []

# Calling Function
evens = getEvenElementsOfArray(l1)

# Printing
print(f"Even Elements of Array : {evens}") # [2,4]