import random

def find_three_numbers_to_a_sum(values, target):
    """
    Finds 3 numbers that add up to a sum
    Returns either null or a list of three values
    Maybe it should return a tuple?
    MUST be three values that sum to sum_target
    """
    
    # TODO: Sanitize sum_target - instance of int
    # Assume values is sorted in ascending order. If not, sort it - nlog(n)
    # Check if < 3 elements in values
    # If values has 3 elements, do a quick check? This should still work though!
    
    for i in range(0, values.__len__()):
        for j in range(values.__len__() - 1, 0, -1):
            # Test some ending conditions
            if (target - values[j] - values[i]) < 0:
                continue
            if (j - i < 1):
                return []
            
            # Now it's possible for middle number to exist
            for k in range(i+1, j - i + 1):
                if (target == values[i] + values[j] + values[k]):
                    return [i, j, k]
    
some_sample_numbers = []

for x in range(0, 100):
    some_sample_numbers.append(random.randint(0, 100))
some_sample_numbers.sort()
sum_target = random.randint(0, 100)

sum_target = 253
some_sample_numbers = [1, 3, 5, 100, 150]

print(some_sample_numbers)
print('Target Sum:', sum_target)

result = find_three_numbers_to_a_sum(some_sample_numbers, sum_target)
if ( (isinstance(result, list)) and (result.__len__() == 3) ):
    print('Result found!', result)
else:
    print('Result not found :(', result)