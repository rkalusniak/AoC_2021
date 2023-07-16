"""
Created: July 15 10:11:31 2023

by: Rachel Kalusniak
"""
#Import libraries
import re
import numpy as np


# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'


# Open code file and strip and split list
with open('code_file.txt', 'r') as f:
    code_input = f.read().rstrip().strip().splitlines()


# Initialize lists
combine_list = []

# Combine the first and second code chunks so each line type is in one string
for i in range(8):
    combine = code_input[i] + ' ' + code_input[i + 9]
    combine_list.append(combine)

# Split string into sublist
combine_list = [re.split(r'\s+', item.strip()) for item in combine_list]

# Get just the first item from the repeated letters and replace in combine_list
for i in range(1,len(combine_list), 3):
    shorten_letters = [letter[0] for letter in combine_list[i]]
    combine_list[i] = shorten_letters

# Combine the two middle characters in code
for i in range(1,8):
    if len(combine_list[i]) > 10:
        combine_list[i] = [a+b for a,b in zip(combine_list[i][0::2], combine_list[i][1::2])]


# Drop lines 3 and 5 because duplicates
combine_list.pop(3)
combine_list.pop(5)


# Initialize a dictionary
clean_code = {}
all_strs = []
all_lens = []

# Loop through the possible outputs
for i in range(10):

    # Create a list for each results 0 to 9
    str_list = [item[i] for item in combine_list[1:]]

    # Join list into single string
    str_combine = ''.join(map(str, str_list))

    # Remove periods
    str_combine = re.sub('\.(?!\d)', '', str_combine)

    # Record string and length
    all_strs.append(str_combine)
    all_lens.append(len(str_combine))

# Combine string and length to dictionary
clean_code['string'] = all_strs
clean_code['length'] = all_lens


# Open txt file and strip and split list
with open(data_file, 'r') as f:
    input = f.read().rstrip().splitlines()
    input = [x.split(' | ') for x in input]


# Initialize lists
output_list = []
signal_list = []

# Break the signals into sub list of strings and removes the pipe character
for i in range(len(input)):
    signal_str = input[i][0].split(' ')
    signal_list.append(signal_str)

# Break the output into a sublist of strings
for i in range(len(input)):
    output_str = input[i][1].split(' ')
    output_list.append(output_str)


# Initialize len list
outputlen_list = []

# Find the length of each string and append to len list. Already stripped extra spaces
for sublist in output_list:
    len_stat = [len(x) for x in sublist]
    outputlen_list.append(len_stat)

# Get a dictionary count of lengths in the flattened output list
count_output_len = {}
for i in range(8):
    count_output_len[i] = list(np.array(outputlen_list).flatten()).count(i)


# Get unique lengths in code
# Create a dictionary with the count for each length
count_code_dict = {}
for i in range(8):
    count_code_dict[i] = clean_code['length'].count(i)

# Initialize dictionary and lists to hold unique lenghts and matching output
unique_len = {}
unique_lengths = []
unique_output = []

# Go through dictionary where instances of length is 1. Look up the position of length in clean code
for length, count in count_code_dict.items():
    if count == 1:
        # Record outputs where the length is unique
        unique_output.append(clean_code['length'].index(length))
        # Record length unique
        unique_lengths.append(length)

# Put results into dictionary
unique_len['length'] = unique_lengths
unique_len['output'] = unique_output

# Count number of unique  lengths in output
count_unique = 0
for i in unique_len['length']:
        count_unique += count_output_len[i]


# Print answer
print(f'The answer is {count_unique:,}.')