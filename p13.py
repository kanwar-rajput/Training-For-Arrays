def deleteTheElementFromStartOfArray(list):
    """
        Removes the element from the start of an Array
    """
    list.pop(0)
    return list
    

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
l1 = deleteTheElementFromStartOfArray(l1)

# Printing
print(f"Array after deleting the first Element : {l1}") # [2,3,4]