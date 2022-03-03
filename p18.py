def getLengthOfArray(list):
    """
        Returns the length of Array
    """
    len = 0
    for _ in list:
        len += 1
    return len

def averageOfArray(list):
    """
        Returns the sum of array.
    """
    sum = 0
    for i in list:
        sum += i

    length = getLengthOfArray(list)
    return sum/length


def getElementsLessThanAverageOfArray(list):
    """
        Returns array of elements which are less than the average of the array
    """
    templist = []
    average = averageOfArray(list)
    for i in list:
        if i<average:
            templist.append(i)
    return templist

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Making Empty list for storing elements
elements = []

# Calling Function
elements = getElementsLessThanAverageOfArray(l1)

# Printing
print(f"Elements lesser than the Average of Array : {elements}") # 1 2