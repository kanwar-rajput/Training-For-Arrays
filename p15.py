def getLengthOfArray(list):
    """
        Returns the length of Array
    """
    len = 0
    for _ in list:
        len += 1
    return len

def deleteTheElementFromMiddleOfArray(list):
    """
        Removes the element from the Middle of an Array
    """
    mid = getLengthOfArray(list)//2
    list.pop(mid)
    return list
    
# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
length = deleteTheElementFromMiddleOfArray(l1)

# Printing length
print(f"Array after deleting the Middle Element : {length}") # [1,2,4]