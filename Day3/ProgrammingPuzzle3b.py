"""
Created: July 14 00:15:22 2023

by: Rachel Kalusniak
"""
# Import libraries
import copy
import numpy as np
from scipy import stats



# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'

# Open txt file and numbers called (zero line) into list
with open(data_file, 'r') as f:
    input = f.read().rstrip().splitlines()


# Break strings into individual values
input = [[*x] for x in input]

# Initialize report list. Don't initialize lists in a loop that is VERY BAD
report = []

# Loop through each row to convert each value to integer
for row in input:
    report.append([int(x) for x in row])


# Convert report to np array
report_array = np.array(report)


# Oxygen generator for most common
#Deep copy
oxygen_array = copy.deepcopy(report_array)

#Loop through columns
for column in range(len(report_array[0])):

    #Get mean of each column
    mean_column = np.mean(oxygen_array[:, column], axis = 0)

    #Convert mean to mode
    if mean_column >= 0.5:
        mode_column = 1
    if mean_column < 0.5:
        mode_column = 0

    # Filter to rows matching mode
    oxygen_array = oxygen_array[oxygen_array.T[column] == mode_column]

    # Break loop if get down to single value
    if len(oxygen_array) <= 1:
        break


# CO2 generator for least common
#Create deep copy
CO2_array = copy.deepcopy(report_array)

#Loop through columns
for column in range(len(report_array[0])):

    # Get mean of each column
    mean_column = np.mean(CO2_array[:, column], axis = 0)

    # Convert mean to least common
    if mean_column >= 0.5:
        least_column = 0
    if mean_column < 0.5:
        least_column = 1

    # Filter to rows matching mode
    CO2_array = CO2_array[CO2_array.T[column] == least_column]

    # Break loop if get down to single value
    if len(CO2_array) <= 1:
        break


# Convert to decimal number
oxygen_rate = int("".join(map(str, oxygen_array[0])), 2)
CO2_rate = int("".join(map(str, CO2_array[0])), 2)

print(oxygen_rate)
print(CO2_rate)


#Print answer
print(f'The answer is {oxygen_rate*CO2_rate}')



