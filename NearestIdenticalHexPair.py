# This script finds the nearest hex value (00 - FF) that has identical
# digits to the input decimal value

import random

# Uses div and floor operations
# Decimal value can be float or int. Force it to be int
def FindNearestHexPair(decimal_value):
    print ('Random value forced to integer: {0}'.format(decimal_value))
    decimal_value = int(decimal_value)
    if (decimal_value < 0):
        return '00'
    if (decimal_value >= 233):
        return 'FF'
    quotient = int(decimal_value) // 16
    remainder = decimal_value % 16
    print('{0} divides into 16 {1} times with {2} remaining.'.format(
        decimal_value, quotient, remainder
    ))
    if (remainder <= 8):
        hex_digit = str(hex(quotient))[2:]
        return hex_digit + hex_digit
    else:
        hex_digit = str(hex(quotient + 1))[2:]
        return hex_digit + hex_digit


random_value = random.randint(0, 255)
result = FindNearestHexPair(random_value)
print('Closest hex number with identical digits is: {0}'.format(result))
