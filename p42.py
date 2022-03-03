def median(list):
    """
        Returns the median of Array
    """
    sortedList = sorted(list)
    length = len(list)
    index = (length - 1) // 2
   
    if (length % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.


# Array
l1 = [99,48,34,57,65,23,54,22,43,21]

# Calling Function
print(f"Median : {median(l1)}") # 45.5