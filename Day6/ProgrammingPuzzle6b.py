"""
Created: July 13 18:20:45 2023

by: Rachel Kalusniak
"""
from collections import Counter

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




# Initialize dictionary with count of values
fish_births = {}

# Create count of initial list. Start at 9 to allow room for first subtraction
for i in range(0, 10, 1):
    fish_births[i] = fish_days.count(i)



# Loop through list until target day
for i in range(256):
    # Perform transformations

    #Count number of new lanternfish to create
    new_count = fish_births[0]

    #Reduce dictionary keys by 1
    fish_keys = [x - 1 for x in list(fish_births.keys())]

    #Recombine keys with values
    fish_births = dict(zip(fish_keys, fish_births.values()))

    #Convert zeros to 6s
    fish_births[6] = fish_births[6] + fish_births[-1]

    #Remove the -1 key from the dictionary
    fish_births.pop(-1)

    #Add 8s for all the zeros counted at the beginning
    fish_births[8] = new_count



# Print answer
print(f'The answer is {sum(fish_births.values())}')



