def factorial(n):
    """
        Returns the factorial of a number
    """
    temp = 1
    for i in range(1,n):
        temp *= i
    return temp

def arrayFactorails(list): # pythonic
    return {list[i] : factorial(list[i]) for i in range(len(list))}

def arrayFactorials2(list):
    """
        Returns the factorail of an Array
    """
    tempdict = {}
    for i,j in enumerate(list):
        tempdict[list[i]] = factorial(j)
    return tempdict

# Array
l1 = [1,2,3,4,5,6]

# Calling the function and storing in dictonary
factorails = arrayFactorials2(l1)

# Printing
print(factorails)

# Pythonic
factorails2 = arrayFactorails(l1)
print(factorails2)