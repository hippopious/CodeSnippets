# This script takes in a series of stock prices and
# figures out, based on hindsight, what the best
# buy and sell strategy will be.
# Restriction: Only one buy and one sell allowed.

import random

# Calculates the best buy and sell prices
# Param: my_data: A list of random integers
# Returns: Buy an Sell price in a dictionary
def CalculateBestBuySellTimes(stock_data):
    # Default to buy and sell on first value (no net loss/gain) - Worst case scenario
    # Guarantees no stock market loss
    # Best gain is expressed by: data[best_sell_index] - data[best_buy_index]
    best_buy_index = 0
    best_sell_index = 0
    try_buy_index = 0
    try_sell_index = 0
    
    # Data checking/cleaning
    if (stock_data.__len__() == 0):
        print('No stock_data. No buy or sell.')
    elif (stock_data[0] == 0):
        raise Exception('First stock datapoint is 0. Unexpected.')
    elif (stock_data.__len__() == 1):
        best_buy_index = stock_data[0]
        best_sell_index = stock_data[0]
        return {'BuyIndex': best_buy_index, 'SellIndex': best_sell_index }
    else:
        # Can fold this into the actual check function too to POTENTIALLY reduce O(n) operations
        for i in range(0, stock_data.__len__()):
            
            # Check data integrity
            if not isinstance(stock_data[i], int):
                raise Exception('Data contains non-int type. Data corrupt.')
                
            # Check company bankruptcy. If company dies, only compute for up to that point
            # Data is clean up to that point, so just take the sublist.
            if (stock_data[i] == 0):
                stock_data = stock_data[0:i]
                print('Company went bankrupt at time:', i, '. Truncating analysis.')
                break
                
            if (stock_data[i] < 0):
                raise Exception('Stock price went below 0. WTF?')
    
    for i in range(0, stock_data.__len__()):
        # Found a global low - Reset both counters to try to find a more optimal buy/sell pair
        if stock_data[i] < stock_data[try_buy_index]:
            try_buy_index = i
            try_sell_index = i
        # Found a better buy/sell pairing. May not be optimal
        if stock_data[i] > stock_data[try_sell_index]:
            try_sell_index = i
        # Comparing to globally best pairing
        # TODO: Optimization: Don't make this check unless we've updated the temporary sell_index
        if ( (stock_data[try_sell_index] - stock_data[try_buy_index]) >
            (stock_data[best_sell_index] - stock_data[best_buy_index]) ):
            
            best_buy_index = try_buy_index
            best_sell_index = try_sell_index
    
    return {'BuyIndex': best_buy_index, 'SellIndex': best_sell_index }

# Generating random data
data = []
for i in range(0, 20):
    data.append(random.randint(0, 100))
print('Random Data: ', data)
    
strategy = CalculateBestBuySellTimes(data)
print('Buy at Index: ', strategy['BuyIndex'], 'at price: ', data[strategy['BuyIndex']])
print('Sell at Index: ', strategy['SellIndex'], 'at price: ', data[strategy['SellIndex']])

print('Random Data at the end: ', data)