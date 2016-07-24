# Python 3

def check_up(array, current_coord, wordchars):
    # some boundary conditions
    if (current_coord[0] + 1 - wordchars.__len__() < 0):
        return False
    counter = 0
    for char in wordchars:
        if (array[current_coord[0]-counter][current_coord[1]] != char):
            return False
        counter = counter + 1
    return True

def check_down(array, current_coord, wordchars):
    pass

def check_left(array, current_coord, wordchars):
    pass

def check_right(array, current_coord, wordchars):
    # some boundary conditions
    if (current_coord[1] + wordchars.__len__() > array[current_coord[0]].__len__()):
        return False
    counter = 0
    for char in wordchars:
        if (array[current_coord[0]][current_coord[1]+counter] != char):
            return False
        counter = counter + 1
    return True

def find_word_occurrences(array, word):
    wordchars = list(word)
    occurrences = 0
    for i in range(0, array.__len__()):
        for j in range(0, array[i].__len__()):
            if (array[i][j] == wordchars[0]):
                if check_up(array, (i, j), wordchars):
                    occurrences = occurrences + 1
                check_down(array, (i, j), wordchars)
                check_left(array, (i, j), wordchars)
                if check_right(array, (i, j), wordchars):
                    occurrences = occurrences + 1
                
    return occurrences
    
# create random array
some_array = [
    ['a', 'e', 'c', 'e', 'e', 'b', 'e'],
    ['a', 'b', 'c', 'e', 'e', 'f', 'g'],
    ['a', 'b', 'c', 'b', 'e', 'e', 'g'],
    ['a', 'b', 'c', 'd', 'b', 'e', 'e']
    ]

some_word = 'bee'

occurrences_found = find_word_occurrences(some_array, some_word)

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