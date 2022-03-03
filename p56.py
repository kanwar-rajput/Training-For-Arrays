def removeVowelsFromArray(list):
    """
        Removes Vowels from Array
    """
    vowels = ['a','e','i','o','u']
    for index,value in enumerate(list):
        if value.lower() in vowels:
            list.pop(index)
    return list

# Array of Characters
l1 = ['A','d','n','a','n']

# Before Removing Vowels
print(f"Before Removing Vowels {l1}")

# Calling Function
l1 = removeVowelsFromArray(l1)

# After
print(f"After Removing Vowels {l1}")