# Python 3.x

# Do it two ways - one with dictionary, one that is in-place

def is_array_circular_using_dictionary(array):
    # This is going to be gross. Going to have a list of Falses
    # Bit array's so much better in Java or C#
    
    # elements_seen (first step)
    # Value  F  T  F  F  F  F
    # Index  0  1  2  3  4  5
    
    elements_seen = []
    curr_index = 0
    
    for i in range(0, array.__len__()):
        elements_seen.append(False)
        
    for index in range(0, array.__len__()):
        next_index = (curr_index + array[curr_index]) % array.__len__()
        if (elements_seen[next_index] == True):
            return False
        else:
            elements_seen[next_index] = True
            curr_index = next_index
    
    return True

def is_array_circular_in_place(array):
    # Check array size > 0, consists of integers
    curr_index = 0
    
    for i in range(0, array.__len__()):
        # curr_index = 0 + 7 % 6 => 1, OR example 2: curr_index = 0 + 0 => 0
        curr_index = (curr_index + array[curr_index]) % array.__len__()
        # If we hit index 0 again and it's not time yet, return False
        if ( (curr_index == 0) and (i != array.__len__() - 1) ):
            return False
    
    return True


# Value  7  2  2  -4   -4   3
# Index  0  1  2   3    4   5

# Value 0
# Index 0

some_array = [7, 2, 2, -4, -4, 3]

print('Array Circular? {0}'.format(is_array_circular_using_dictionary(some_array)))
print('Array Circular? {0}'.format(is_array_circular_in_place(some_array)))
