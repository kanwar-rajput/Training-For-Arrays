def doubleElementOfArray(list):
    """
        Doubles the Elements of Array    
    """
    for index,value in enumerate(list):
        list[index] = value*2
    return list

# Arrays
l1 = [1,2,3,4]

# Printing
print(f"Before Doubling : {l1}")

# Calling Function
doubleElementOfArray(l1)

# Printing
print(f"After Doubling : {l1}")