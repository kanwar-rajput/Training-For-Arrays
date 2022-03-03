def getLengthOfArray(list):
    """
        Returns the length of Array
    """
    len = 0
    for _ in list:
        len += 1
    return len

def getMiddleElementOfArray(list):
    """
        Returns the Middle element of an Array
    """
    mid = getLengthOfArray(list)//2
    return list[mid]

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
mid = getMiddleElementOfArray(l1)

# Printing
print(f"Middle Element : {mid}") # 3