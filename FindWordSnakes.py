# Python 3
# Convention - x increases going down, y increases going right

def find_words(array, wordchars_fragment, x, y, locations_seen):
    # Check conditions where the current element does not continue the word
    occurrences_found = 0
    if (
        (x < 0) or 
        (y < 0) or
        (x >= array.__len__()) or
        (y >= array[x].__len__()) or
        (array[x][y] != wordchars_fragment[0]) or
        (x, y) in locations_seen
    ):
        return occurrences_found
        
    # This is when we find a match for the letter we're looking for at this stage.
    # If the word is done, we return a 1. Otherwise, recurse.
    if (wordchars_fragment.__len__() == 1):
        # We found a word.
        print(x, y)
        return 1
        
    # We have a match, but we need to look for the next letter in all directions
    # Do it blindly here. We check for conditions at the beginning of function
    locations_seen.append((x, y))
    occurrences_found = occurrences_found + find_words(array, wordchars_fragment[1:], x-1, y, locations_seen)
    occurrences_found = occurrences_found + find_words(array, wordchars_fragment[1:], x+1, y, locations_seen)
    occurrences_found = occurrences_found + find_words(array, wordchars_fragment[1:], x, y-1, locations_seen)
    occurrences_found = occurrences_found + find_words(array, wordchars_fragment[1:], x, y+1, locations_seen)
    # We're done with this pixel, whether we found word(s) or not.
    locations_seen.remove((x, y))
    return occurrences_found

def find_word_snakes_occurrences(array, word):
    # Passing this mutable list recursively.
    # When we find a match, we add to it. Decrement this when that branch is done
    # Check conditions on word
    wordchars = list(word)
    locations_in_string = []
    occurrences_found = 0
    # for each element, begin recursion
    for i in range(0, array.__len__()):
        for j in range(0, array[i].__len__()):
            occurrences_found = occurrences_found + find_words(array, wordchars, i, j, locations_in_string)
    
    return occurrences_found
    
# create random array
some_array = [
    ['a', 'e', 'c', 'e', 'e', 'b', 'e'],
    ['a', 'b', 'c', 'e', 'e', 'f', 'g'],
    ['a', 'b', 'c', 'b', 'e', 'e', 'g'],
    ['a', 'b', 'c', 'd', 'b', 'e', 'e']
    ]

some_word = 'beeee'

occurrences_found = find_word_snakes_occurrences(some_array, some_word)

print('Occurrences of {0} found was: {1}'.format(some_word, occurrences_found))

# Test Cases:
# Borders
# fragments
# same starting letter
# Performance? This can be parallelized!
# Assumes m x n array. Irregular array will have index issues. Make check before each hit. If OOB, return false
# Algo only works on left-aligned arrays. With check above, this will work for diff-aligned arrays
# Python 3 means UTF-8 encoding for strings by default.
# Case of letters may be invarient
# Assumes no wraparounds
# Complexity: Each element x 4 directions x word length + some checks --> O(n) time