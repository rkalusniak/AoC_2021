"""
Created: July 14 20:18:23 2023

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


# Create a list of the amount of fuel required up to 0 to max distance
# Initialize with first value. 0 fuel required to move 0 places
fuel_bydistance = [0]

# Loop until get to the furthest crab location from zero plus 1 to accomodate looping below
for i in range(1,max(crab_location) + 1):

    # Fuel use is the previous value in list plus position in list
    fuel_bydistance.append(fuel_bydistance[i - 1] + i)


# Initialize list of total fuel usage
fuel_use = []

# Loop through all crab locations to find the best spot
for j in range(max(crab_location)):

    # Initalize list to hold fuel use per crab at this test point
    test_point = []

    # Loop through each crab
    for crab in crab_location:

        # Find the distance the crab must travel to this test point.
        # Then, find the fuel usage from the fuel_bydistance list
        test_point.append(fuel_bydistance[abs(crab - j)])

    # Sum all the fuel usage for this test point and append to list
    fuel_use.append(sum(test_point))


# Print answer for min fuel use. Don't care about position
print(f'The minimum fuel use is {min(fuel_use):,}.')