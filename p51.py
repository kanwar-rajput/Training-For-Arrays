def isArrayPalindrome(list): # Pythonic
    """
        Returns whether an Array is Palindrome
    """
    return list==list[::-1]

def isArrayPalindrome2(list):
    """
        Returns whether an Array is Palindrome
    """

    templist = []

    # Reversing the list
    for i in range(len(list)-1,-1,-1):
        templist.append(list[i])

    # Comparing Elements of both arrays
    for i in range(len(list)):
        if list[i] != templist[i]:
            return False

    return True

# Arrays
l1 = [1,2,2]
l2 = [1,2,1]

# Calling Function
print(f"Is this Array Palindrome : {isArrayPalindrome(l1)}")
print(f"Is this Array Palindrome : {isArrayPalindrome2(l2)}")