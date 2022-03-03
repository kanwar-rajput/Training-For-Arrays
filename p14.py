def deleteTheElementFromEndOfArray(list):
    """
        Removes the element from the end of an Array
    """
    list.pop(-1)
    return list
    

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
l1 = deleteTheElementFromEndOfArray(l1)

# Printing
print(f"Array after deleting the Last Element : {l1}") # [1,2,3]