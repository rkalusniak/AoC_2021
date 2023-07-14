"""
Created: July 13 18:20:45 2023

by: Rachel Kalusniak
"""

# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'



# Open txt file and strip and split list
with open(data_file, 'r') as f:
    input = f.read().rstrip().split(',')

# Convert list to integers
fish_days = [int(i) for i in input]



# Initialize dictionary for storing results
fish_births = {}


# Loop through list until target day
for i in range(81):

    # Write list to dictionary. Then, make all the changes for the next list
    fish_births[i] = fish_days

    # Count number of fish birthing new laternfish
    new_count = fish_days.count(0)

    # Reduce entire list by 1
    fish_days = [x - 1 for x in fish_days]

    # Add new fish to list based on number of zeros
    fish_days = fish_days+ [8]*new_count

    # Replace negative 1 with 6 days until next birth
    fish_days = [6 if x == -1 else x for x in fish_days]


# Print answer
print(f'The answer is {len(fish_births[80])}')


