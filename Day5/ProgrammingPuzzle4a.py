"""
Created: June 2 23:32:17 2023

by: Rachel Kalusniak
"""
import numpy as np
import pandas as pd

# Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'

# Open txt file and numbers called (zero line) into list
with open(data_file, 'r') as f:
    input = f.read().rstrip().splitlines()


# Initalize lines and coord list
cord_list = []

# Format input
for line in input:
    # Split on the arrow
    line = line.split(" -> ", 1)
    # Split coordinates to tuple integers
    # Reference:
    # https://stackoverflow.com/questions/62752034/transform-string-of-coordinates-stored-in-a-tuple-into-list
    line = np.array([tuple(int(i) for i in point.split(",")) for point in line])
    # Append to end list. We now have a list of lists with tuples inside
    cord_list.append(line)


# Initalize list for line direction
x_match = []
y_match = []

#x_match is true if vertical line. y_match is true if horizontal line
for sublist in cord_list:
    # Create a tuple of x/y values. Test if number of unique values is 1 (ie: x values match). Returns boolean
    # References:
    # https://www.geeksforgeeks.org/python-get-first-element-in-list-of-tuples/
    # https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
    x_match.append(len(set(list(zip(*sublist))[0])) <= 1)
    y_match.append(len(set(list(zip(*sublist))[1])) <= 1)



#Initialize list for line length
line_length = []

# Compute line length
for i in range(0, len(cord_list)):
    if x_match[i] is True:
        line_length.append(np.max(cord_list[i][:, 1]) - np.min(cord_list[i][:, 1]))
    elif y_match[i] is True:
        line_length.append(np.max(cord_list[i][:, 0]) - np.min(cord_list[i][:, 0]))
    #If line is a point (start and stop are the same), length is 0
    elif x_match[i] + y_match[i] == 1:
        line_length.append(0)
    #If diagonal line input line length as none
    elif x_match[i] + y_match[i] == 0:
        line_length.append(None)



def all_points(i, val_num, rep_num):
    """
    Finds all the points between two a starting and ending point
    Parameters
    """

    #Find min and max values for steping
    min_val = np.min(cord_list[i][:, val_num])
    max_val = np.max(cord_list[i][:, val_num])

    #Create a list of steped and repeated values
    step_points = np.arange(min_val, max_val + 1, dtype=int, step=1)
    repeat_points = np.repeat(cord_list[i][0, rep_num], line_length[i] + 1)

    #Initalize array for lists
    subarray = np.zeros((line_length[i] + 1, 2), dtype=int)

    #Add lists to array in the correct position
    subarray[:,val_num] = step_points
    subarray[:,rep_num] = repeat_points
    return subarray

#Initalize list to hold results
all_cord = []
for i in range(0, len(cord_list)):
    #If diagonal line skip and restart loop
    if line_length[i] is None:
        continue
    #If line length 1 or 0 just add the current points to the list
    elif line_length[i] <= 1:
        all_cord.append(cord_list[i])
    #If horizontal or vertical line of length greater than 1, add all points to the array
    elif line_length[i] > 1:
        if x_match[i] is True:
            all_cord.append(all_points(i, 1, 0))
        if y_match[i] is True:
            all_cord.append(all_points(i, 0, 1))


#Flatten the list into a single dataframe
flat_all_cord = pd.DataFrame(np.concatenate(all_cord), columns = {'xval', 'yval'})


#Initalize duplicate counter dataframe
duplicates = pd.DataFrame()

#Count duplicates
duplicates['count_hits'] = flat_all_cord.pivot_table(index = ['xval', 'yval'], aggfunc ='size')
#Reset to manipulatable dataframe
duplicates.reset_index(inplace = True)
#Create a list of just points with repeates
dup_count = duplicates[duplicates['count_hits'] >= 2]

#Print the results
print(f'There are {len(dup_count)} points where 2 or more lines intersect.')