from random import randint as RAND

def getRandomIndex(list):
    """
        Returns the Random element index of an Array
    """
    return RAND(0,len(list))

# Declaring and Initializing List / Array
l1 = [1,2,3,4]

# Calling the function
rand = getRandomIndex(l1)

# Printing
print(f"Random Index : {rand}") # 0 | 1 | | 2 | 3