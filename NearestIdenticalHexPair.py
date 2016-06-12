# This script finds the nearest hex value (00 - FF) that has identical
# digits to the input decimal value

import random

possible_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Uses div and floor operations
# Decimal value can be float or int. Force it to be int
def FindNearestHexPair(input_string):

    print('Input is:', input_string)

    if (input_string.__len__() != 6):
        raise Exception('Input does not have length of 6 - It is not 3 pairs of hex values. WTF')

    for x in range(0, input_string.__len__()):
        if (input_string[x] not in possible_values):
            raise Exception('Input at index {0} contains out of range data: {1}.'.format(
                x, input_string[x]
            ))

    # This is what we're returning. We'll append to this.
    paired_values = []

    # x = 0, 1, 2. Need indices 0-1, 2-3, 4-5
    for x in range(0, 3):
        current_value = input_string[x*2:x*2+2]
        print('Current Value being operated on is: {0}. Dec: {1}'.format(
            current_value, int(current_value, 16)
        ))

        # Set some simple boundary conditions
        if (int(current_value, 16) > 248):
            paired_values.append('ff')
            continue
        if (int(current_value, 16) <= 8):
            paired_values.append('00')
            continue

        # Lower and upper bounds are different
        # depending on whether the first or second hex digit is bigger
        if (int(current_value[1], 16) > int(current_value[0], 16)):
            lower_value = current_value[0]
            if (int(current_value[0], 16) >= 15):
                raise Exception('Value overflow if increased:', int(current_value[0], 16))
            higher_value = hex(int(current_value[0], 16) + 1)[2:]
        else:
            higher_value = current_value[0]
            if (int(current_value[0], 16) <= 0):
                raise Exception('Value negative if decreased', int(current_value[0], 16))
            lower_value = hex(int(current_value[0], 16) - 1)[2:]

        # Take the first hex digit and duplicate it.
        # These are the comparison values
        lower_value = lower_value + lower_value
        lower_value_dec = int(lower_value, 16)
        print('Lower value to compare against: {0}. Dec: {1}'.format(
            lower_value, lower_value_dec
        ))
        higher_value = higher_value + higher_value
        higher_value_dec = int(higher_value, 16)
        print('Higher value to compare against: {0}. Dec: {1}'.format(
            higher_value, higher_value_dec
        ))

        if (int(current_value, 16) - lower_value_dec <= 8):
            paired_values.append(lower_value)
        else:
            paired_values.append(higher_value)

    return ''.join(paired_values)


# Populating the random input
# Format : A0FFC2
# This is overly complicated. We can just append to a list and then join.
random_value = '000000'
random_value_list = list(random_value)
for  x in range(0, 6):
    random_value_list[x] = possible_values[random.randint(0, possible_values.__len__()-1)]
random_value = ''.join(random_value_list)

result = FindNearestHexPair(random_value)
print('Processed hex sequence: {0}'.format(result))
