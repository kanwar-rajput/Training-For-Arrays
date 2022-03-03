def arrayOfFibonacci(n):
    """
        Returns the fibonacci numbers and it's sum
    """
    temp = 0
    templist = []
    for _ in range(n):
        temp += 1
        templist.append(temp)
    return templist,sum(templist) # Returning two elements from function

# Declaring List / Array for storing Fibonaccis
l1,size = arrayOfFibonacci(10) # Calling Function

print(f"Fibonacci Series : {l1} = {size}" )