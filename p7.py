def getLengthOfArray(list):
    """
        Returns the length of Array
    """
    len = 0
    for _ in list:
        len += 1
    return len


# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
length = getLengthOfArray(l1)

# Printing length
print(f"The Length of the Array is : {length}") # 4