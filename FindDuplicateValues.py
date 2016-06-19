# Python 3.x

import random

# Takes in a list of integers and returns a dictionary containing
# values that occur more than once and its actual occurrence value
def FindDuplicateValues(input):
    # TODO: Check all values of input for integer isinstance
    print('Input is: {0}'.format(input))

    # Tally everything up
    occurrences = {}
    for number in input:
        if number in occurrences.keys():
            occurrences[number] = occurrences[number] + 1
        else:
            occurrences[number] = 1
    
    # Find what to kill
    delete_list = []
    for key, value in occurrences.items():
        if (value == 1):
            delete_list.append(key)

    # Wipe what we need
    for key in delete_list:
        del occurrences[key]

    # TODO: Might want to check output before returning if we need to be uber sure
    return occurrences
    
# Generate some values and that jazz
randomValues = []
for i in range(0, 10):
    randomValues.append(random.randint(0, 5))

result = FindDuplicateValues(randomValues)
print('Result is: {0}'.format(result))


# Sample Results:

# C:\repos\CodeSnippets>python FindDuplicateValues.py
# Input is: [0, 4, 3, 3, 0, 0, 2, 4, 1, 3]
# Result is: {0: 3, 3: 3, 4: 2}

# C:\repos\CodeSnippets>python FindDuplicateValues.py
# Input is: [1, 0, 2, 0, 3, 5, 1, 2, 4, 2]
# Result is: {0: 2, 1: 2, 2: 3}

# C:\repos\CodeSnippets>python FindDuplicateValues.py
# Input is: [2, 0, 3, 3, 0, 0, 3, 1, 3, 4]
# Result is: {0: 3, 3: 4}