# Python 3.5.x
# Solution to finding the longest substring inside a string of unique elements

# Speed complexity at the function's stack level is O(n).
# However, under the hood, because of hash searching,
# this CAN devolve to O(n^2) if all elements are unique and the hashing sucks.
# In this case, for each element, the dictionary search has to go over
# 'all' elements in dictionary.
# One way to avoid this is to write our own hash array/list, containing all
# possible values and restricting/shrinking the problem space. No hash searching
# will happen and hashing in will be guranteed to be O(1).
# More memory required in that case. Either way, memory requirements is still O(n).

import random

# Finds the longest substring inside an input string
# param: input_string: a string of instance str.
# returns: dictinary containing the start and end indices for the longest substring
def FindLongestSubstring(input_string):
    result = []

    # This line is totally for fun. Now I know how to split/join strings/lists
    input_array = "".join(list(input_string))
    print('Input is:', input_array)

    # Boundary counditions. Ensure algo operates on longer strings
    if ( (not isinstance(input_string, str)) or (input_string.__len__() == 0) ):
        return ''
    elif (input_string.__len__() == 1):
        return input_string

    # String is sanitized and has size of 2+. Initializing values.
    best_start = 0
    best_end = 1
    best_size = 1
    cur_start = 0
    cur_size = 1

    # A dictionary of characters and when they were last seen. Initilize it.
    seen_chars = {
        input_string[0]: 0
    }

    for cur_end in range(1, input_string.__len__()):
        cur_char = input_string[cur_end]
        if cur_char in seen_chars.keys():
            # We've hit a duplicate char. May not be a problem
            # Not possible to hit a global best (highscore!) if we hit a dupe
            if (seen_chars[cur_char] >= cur_start):
                print('At index {0}: cur_start changing from {1} to {2}'.format(
                    cur_end,
                    cur_start,
                    seen_chars[cur_char]+1
                ))
                cur_start = seen_chars[cur_char] + 1
                print('At index {0}: cur_size changing from {1} to {2}'.format(
                    cur_end,
                    cur_size,
                    cur_end - cur_start + 1
                ))
                cur_size = cur_end - cur_start + 1
                # Guard against end of string condition
                # The fact that this value was seen in the dictionary
                # means that the start index cannot be > end index.
                # Still, let's use >= to guard
                if (cur_start >= input_string.__len__() - 1):
                    return {'start': int(best_start), 'end': int(best_end)}
            else:
                # We found a dupe but the dupe occurs before our current start pt
                cur_size = cur_size + 1
            # Update this last after potential calculations
            print('At index {0}: Dictionary entry of char {1} changing from {2} to {3}'.format(
                cur_end,
                cur_char,
                seen_chars[cur_char],
                cur_end
            ))
            seen_chars[cur_char] = cur_end
        else:
            # Found a unique-char (so far). Add it to the dictionary
            seen_chars[cur_char] = cur_end
            cur_size  = cur_size + 1

        # Update best values. If we found a dupe, this won't happen
        if (cur_size > best_size):
            best_size = cur_size
            best_start  = cur_start
            best_end = cur_end

    return {'start': int(best_start), 'end': int(best_end)}


# Main
rand_string = []

# Get some lower-case characters in there
# Python can't do in-place replace efficiently
for x in range(0, 30):
    rand_string.append(chr(random.randint(97, 26+97)))
rand_string = ''.join(rand_string)

result = FindLongestSubstring(rand_string)

print('Longest substring starts at {0}, ends at {1}, and is {2}'.format(
    result['start'],
    result['end'],
    rand_string[result['start']:result['end']+1]
))

# Sample output
# Input is: tissqn{{pg{ke{wfxnccky{ncn{hrv
# At index 3: cur_start changing from 0 to 3
# At index 3: cur_size changing from 3 to 1
# At index 3: Dictionary entry of char s changing from 2 to 3
# At index 7: cur_start changing from 3 to 7
# At index 7: cur_size changing from 4 to 1
# At index 7: Dictionary entry of char { changing from 6 to 7
# At index 10: cur_start changing from 7 to 8
# At index 10: cur_size changing from 3 to 3
# At index 10: Dictionary entry of char { changing from 7 to 10
# At index 13: cur_start changing from 8 to 11
# At index 13: cur_size changing from 5 to 3
# At index 13: Dictionary entry of char { changing from 10 to 13
# At index 17: Dictionary entry of char n changing from 5 to 17
# At index 19: cur_start changing from 11 to 19
# At index 19: cur_size changing from 8 to 1
# At index 19: Dictionary entry of char c changing from 18 to 19
# At index 20: Dictionary entry of char k changing from 11 to 20
# At index 22: Dictionary entry of char { changing from 13 to 22
# At index 23: Dictionary entry of char n changing from 17 to 23
# At index 24: cur_start changing from 19 to 20
# At index 24: cur_size changing from 5 to 5
# At index 24: Dictionary entry of char c changing from 19 to 24
# At index 25: cur_start changing from 20 to 24
# At index 25: cur_size changing from 5 to 2
# At index 25: Dictionary entry of char n changing from 23 to 25
# At index 26: Dictionary entry of char { changing from 22 to 26
# Longest substring starts at 11, ends at 18, and is ke{wfxnc



# Scratch: (not updated)
# best start index (update whenever working best better)
# best end index (update whenever working best is better)
# working start index (update when we find a dupe. update to index of the duped element + 1) - check size
# working end index (increment every time) <- this is current
# working size (increment every time we encounter a different char that doesn't exist in library)
# best size (increment when working size > best size)
# a b c d e f g c y z b w
# c c
