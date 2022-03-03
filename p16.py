def sumOfArray(list):
    """
        Function to print the elements of array.
    """
    sum = 0
    for i in list:
        sum += i
    return sum

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the Function
size = sumOfArray(l1)

# Printing
print(f"The sum of array : {size}") # 10