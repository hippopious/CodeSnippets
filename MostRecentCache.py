# Cache system. Will take in ID's that returns something from the database
# If hotel isn't on the list already, then check max size of cache. If smaller, append. Otherwise, pop the least recent one and then append
# If hotel IS on the list already, pop the element and append. Size of cache doesn't change.

# Dictionary that maps 

import random

class most_recent_cache:
    
    def __init__(self, size):
        # Solely for quick retrieval of data
        self.hotel_lookup = {}
        # Contains hotel data and most-recent ordering
        # Most recent is at the end, least recent is at the front
        self.hotel_data = []
        self.max_size = size
        
    def find_hotel(self, hotel_id):
        try:
            hotel_data_location = self.hotel_lookup[hotel_id]
            # This only works in Python because our payload is a string, not a list or dictionary or complex data structure
            hotel_data_payload = self.hotel_data[hotel_data_location][1]
            self.hotel_data.pop(hotel_data_location)
            self.hotel_data.append((hotel_id, hotel_data_payload))
            self.hotel_lookup[hotel_id] = self.hotel_data.__len__()-1
            
            return self.hotel_data[self.hotel_data.__len__()-1][1]
        except KeyError:
            # Generating fake data. This would normally be coming from a database
            some_random_hotel_data = [random.randint(0, 50) for i in range(0, 5)]
            some_random_hotel_data = [str(value) for value in some_random_hotel_data]
            some_random_hotel_data = ''.join(some_random_hotel_data)
            # print('Random hotel data about to be added: {0}'.format(some_random_hotel_data))
            if (self.hotel_data.__len__() < self.max_size):
                # Append tuple and add to dictionary
                self.hotel_data.append((hotel_id, some_random_hotel_data))
                self.hotel_lookup[hotel_id] = self.hotel_data.__len__()-1
            elif (self.hotel_data.__len__() == self.max_size):
                # Remove least recent (array + LU), and append new entry
                hotel_to_remove = self.hotel_data[0][0]
                self.hotel_data.pop(0)
                del self.hotel_lookup[hotel_to_remove]
                
                self.hotel_data.append((hotel_id, some_random_hotel_data))
                self.hotel_lookup[hotel_id] = self.hotel_data.__len__()-1
            else:
                raise Exception('Cache exceeded max size')
                
            return some_random_hotel_data
            
    
# Main run

hotel_cache = most_recent_cache(10)

print(hotel_cache.find_hotel(11))
print(hotel_cache.find_hotel(22))
print(hotel_cache.find_hotel(33))
print(hotel_cache.find_hotel(44))
print(hotel_cache.find_hotel(55))
print(hotel_cache.find_hotel(66))
print(hotel_cache.find_hotel(77))
print(hotel_cache.find_hotel(88))
print(hotel_cache.find_hotel(99))
print(hotel_cache.find_hotel(1010))
print(hotel_cache.find_hotel(1111))
#print(hotel_cache.find_hotel(77))
#print(hotel_cache.find_hotel(44))
print('the whole array looks like: {0}'.format(hotel_cache.hotel_data))
print('the dictionary looks like: {0}'.format(hotel_cache.hotel_lookup))