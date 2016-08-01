import random

seed = [1, 2, 3, 4]

random_numbers = [random.randint(0,10) for i in range(0, 20)]
print(random_numbers)

# Nice. List comprehensions above.

# Now we want to practice avoiding dots in the looooooop

generate_random_int = random.randint
random_numbers = [generate_random_int(0, 10) for i in range(0, 20)]
print(random_numbers)

# Now we want to update a dictionary

dict1 = {"item1": "Goat Cheese", "item2": "Jam Fool", "item3": "Jericho beach"}

dict1.update(dict1)

print(dict1)