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
        Returns the Average of Array.
    """
    sum = 0
    for i in list:
        sum += i

    length = getLengthOfArray(list)
    return sum/length

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling Function
average = averageOfArray(l1)

# Printing
print(f"The Average of array : {average}") # 2.5