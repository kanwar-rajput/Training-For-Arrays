def getLengthOfArray(list):
    """
        Returns the legnth of Array
    """
    temp = 0 
    for _ in list:
        temp += 1
    return temp

def sameLengthArrays(list1 , list2):
    """
        Checks whether two arrays have same length
    """
    if getLengthOfArray(list1) == getLengthOfArray(list2):
        print("They have same length")
    else:
        print("They don't have same length")

# Declaring and Initializing List / Array
l1 = [1,2,3,4]
l2 = [1,2,3]
l3 = [3,4,5,6]

# Calling Function for l1,l2
sameLengthArrays(l1,l2) # They don't have same length

# Calling Function for l1,l3
sameLengthArrays(l1,l3) # They have same length