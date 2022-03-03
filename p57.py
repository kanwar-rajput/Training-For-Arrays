def isEqual(list1 , list2):
    """
        Tells whether Two Arrays have same elements
    """
    if (len(list1) != len(list2)):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
    return True

# Arrays
l1 = [1,2,3,4]
l2 = [2,3,4,5]
l3 = [1,2,4,3]  # although   l1 and l3 have same elements  yet the testcase is false
l4 = [1,2,3]

# Test Case 1
print(isEqual(l1,l2))

# Test Case 2
print(isEqual(l1,l3))

# Test Case 3
print(isEqual(l1,l4))