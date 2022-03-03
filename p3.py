def revArray(list):
    """
        Write a function to Return the Reverse of the array
    """
    templist = []
    for i in range((len(list)-1),-1,-1):
        templist.append(list[i])
    return templist


# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Empty List / Array
l2 = []

# Calling Function
l2 = revArray(l1)

# Printing Array
print(f"The reversed array : {l2}") # [4,3,2,1]