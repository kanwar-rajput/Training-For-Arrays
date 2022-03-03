def compare2Arrays(list1 , list2):
    """
        Compares if two Arrays are equal or not in sequence
    """
    status = 0
    if len(list1) != len(list2):
        print("They are not equal in Sequence")
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                status += 1
        if (status != 0):
            print("They are not equal in sequence")
        else:
            print("They are equal in sequence")


# Declaring and Initializing List / Array
l1 = [1,2,3,4]
l2 = [1,2,3]
l3 = [1,2,3,4]
l4 = [1,2,3,5]

# Calling Function
compare2Arrays(l1,l2) # They are not equal in sequence

# Calling Function for l1,l3
compare2Arrays(l1,l3) # They are equal in sequence

# Calling Function for l1,l4
compare2Arrays(l1,l4) # They are not equal in sequence