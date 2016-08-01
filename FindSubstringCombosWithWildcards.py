# Python 3.x

import random

def seek_substring(possible_substrings, input, location):
    # Make sure the location is within bounds. If out of bounds, we're done.
    # If valid location in list, add possibilities to running total.
    # Based on character, call this method recursively once or twice
    
    if (location >= input.__len__()):
        return 
    
# Return all string combinations
def find_substring_combos(string_input):
    possible_substrings = []
    
    # Check string for invalid entries
    # Size integrity checks - 0 size, 1 size - check for '?' though!
    
    input = list(string_input)
    
    # Blindly throw elements into the recursion method. The recursion method
    # will check for boundaries
    for i in range(0, input.__len__()):
        seek_substring(possible_substrings, input, i)
    
    return possible_substrings

string_input = []

for i in range(0, 10):
    rand_int = random.randint(0, 2)
    if (rand_int == 0):
        string_input.append('0')
    elif (rand_int == 1):
        string_input.append('1')
    elif (rand_int == 2):
        string_input.append('?')
    else:
        raise Exception('Died.')

string_input = ''.join(string_input)

print('Input is: {0}'.format(string_input))