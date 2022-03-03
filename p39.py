def isPrime(num):
    """
        Checks Whether a number is Prime
    """
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def getPrimes(list):
    """
        Returns Primes in Array
    """
    templist = []
    for i in list:
        if isPrime(i):
            templist.append(i)
    return templist

# Array
l1 = list(range(10))

# Calling Function
print(getPrimes(l1)) # [2,3,5,7]