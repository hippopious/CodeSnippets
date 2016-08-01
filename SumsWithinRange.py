

def find_pairs_that_sum_within_range(array, sum_range):
    # Outer loop - We'll likely return before this, but you never know
    right_starting_index = array.__len__() - 1
    pairs_found = []
    for i in range(0, array.__len__()):
        # Initial conditions. Here is where we update starting cursor or break from the loop
        if (right_starting_index < i):
            raise Exception('Something died. It smells. - Something more intelligent')
        if (right_starting_index == i):
            # We're done. No more combinations to check
            return pairs_found
        cursor = right_starting_index
        
        while (cursor > i):
            sum = array[i] + array[cursor]
            if (sum > sum_range[1]):
                # There's no point looking at this right index anymore since 'i' will only stay the same or increase
                right_starting_index -= 1
                # Add this escape clause here. The outer loop will increment i after this loop ends, making i > right_starting_index
                if (right_starting_index == i):
                    return pairs_found
                cursor -= 1
                continue # More values may exist to the left of cursor
            
            if (sum < sum_range[0]):
                cursor -= 1
                break # we're done with this value of i
            
            if (sum >= sum_range[0] and sum <= sum_range[1]):
                # In range.
                print('Found pair! {0}, {1}'.format(i, cursor))
                pairs_found.append((array[i], array[cursor]))
            
            cursor -= 1
            
        

# main

# We'll sort it (nlog(n))

some_array = [-3, 0, 1, 3, 5, 5, 7, 13]
the_range = (8, 12)

all_pairs = find_pairs_that_sum_within_range(some_array, the_range)
print(all_pairs)
print('Pairs found: {0}'.format(all_pairs.__len__()))

