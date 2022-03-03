def isArrayEmpty(list):
    """
        Tells whether an Array is empty
    """
    return False if len(list)==0 else True

# Arrays
l1 = [1,2,3]
l2 = []

# Checking
print(f"Is this Array Empty : {isArrayEmpty(l1)}")
print(f"Is this Array Empty : {isArrayEmpty(l2)}")
