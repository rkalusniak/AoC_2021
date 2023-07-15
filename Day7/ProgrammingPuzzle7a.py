"""
Created: July 14 19:33:45 2023

by: Rachel Kalusniak
"""
# Import libraries
import numpy as np

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
crab_location = [int(i) for i in input]


#Initalize list
fuel_use = []

# Loop through all positions from 0 to max of list
for i in range(max(crab_location)):

    #Find the fuel use for each crab to move to position i in absolute value. Then sum total fuel use
    fuel_use.append(sum([abs(crab - i) for crab in crab_location]))

# Print answer for min fuel use. Don't care about position right now
print(f'The minimum fuel use is {min(fuel_use):,}.')