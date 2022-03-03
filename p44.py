def elementCountInArray(list,element):
    """
        Returns how many times an element is in the array 
    """
    temp = 0
    for i in list:
        if i == element:
            temp += 1
    return temp

# Array
l1 = [1,2,3,3,3,4]

print(f"Total Times Element in Array : {elementCountInArray(l1,3)}") # 3

