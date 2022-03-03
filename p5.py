def getMinOfArray(list):
    """
        Returns the min of list
    """
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the Function
min = getMinOfArray(l1)

# Printing the lowest element
print(f"The Lowest element of the Array : {min}") # 1