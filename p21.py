from distutils.util import subst_vars

def subStrOfArray(list,substr):
    """
        Returns the substring of Array
    """
    if not substr > (len(list)-1):
        return list[substr]
    else:
        return -1

# Array
l1 = [1,2,3]

# Calling Function
substr = subStrOfArray(l1,2)

# Printing
print(substr)