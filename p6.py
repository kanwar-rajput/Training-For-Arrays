def getMaxOfArray(list):
    """
        Returns the max of list
    """
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the Function
max = getMaxOfArray(l1)

# Printing the highest element
print(f"The highest element is : {max}") # 4