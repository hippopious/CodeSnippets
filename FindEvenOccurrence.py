# Python 3.x
# Pretty important for dictionary item referencing

# Find the element that occurs an even number of times.
# Being lazy with checks
def FindEvenOccurrence(input):
    print('Input: {0}'.format(input))

    # Check input for data integrity and stuff. Lazying.

    occurrences = {}
    for number in input:
        if number in occurrences.keys():
            occurrences[number] = occurrences[number] + 1
        else:
            occurrences[number] = 1
    
    for key, value in occurrences.items():
        if ( (value % 2) == 0 ):
            print("Input {0} has {1} occurrences.".format(key, value))

numbers = []
numbers.append(3)
numbers.append(4)
numbers.append(4)
numbers.append(2)
numbers.append(8)
numbers.append(4)
numbers.append(3)
numbers.append(8)
numbers.append(2)
numbers.append(3)
numbers.append(8)
numbers.append(3)
numbers.append(3)

FindEvenOccurrence(numbers)

# Output:

# C:\repos\CodeSnippets>python FindEvenOccurrence.py
# Input: [3, 4, 4, 2, 8, 4, 3, 8, 2, 3, 8, 3, 3]
# Input 2 has 2 occurrences.