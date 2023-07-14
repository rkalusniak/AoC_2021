"""
Created: July 13 21:39:17 2023

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


# Calculate most common value and second most common value
# Get mean value of each column
mean_columns = np.mean(report_array, axis=0)

# Initalize the list for most common values
gamma_list = []         #Gamma is most common
epsilon_list = []       #Epsilon is second

# Convert mean value to 0 or 1 as most common
for i in range(len(mean_columns)):
    if mean_columns[i] < 0.5:
        gamma_list.append(0)
        epsilon_list.append(1)
    if mean_columns[i] > 0.5:
        gamma_list.append(1)
        epsilon_list.append(0)

# Turn list into binary number then base 10 number
gamma_rate = int("".join(map(str, gamma_list)), 2)
epsilon_rate = int("".join(map(str, epsilon_list)), 2)


# Print answer
print(f'The answer is {gamma_rate*epsilon_rate}')


