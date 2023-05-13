"""
Created on Sat May 15  10:28:33 2023

@author: Rachel Kalusniak
"""

import numpy as np


#Create a function to find the  step direction of a list
def AOC1b(deapthfile):
    """
    Use a list and check if the next value is an increase or decrease.


    Parameters
    ----------
    deapthfile : txt file
        Input txt file of numbers of elevation of sea floor

    Returns the number of increasing elevations


    """
    # Reading in txt file
    with open(deapthfile, 'r') as f:
        data = f.read()
        data = data.rstrip()
        seafloor_list = data.split('\n')

    #Convert the list of strings to integers
    seafloor_list = [int(i) for i in seafloor_list]

    #seafloor_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    # Find the number of items in the seafloor list allowing for variability
    length = len(seafloor_list)

    seafloor_moving3_list = []
    for i in range(0, length - 2):
        seafloor_moving3_list.append(seafloor_list[i] + seafloor_list[i + 1] + seafloor_list[i + 2])

    # Initialize a secondary list with the previous value in the same position.
    # The first value is zero because there is no previous value.
    seafloor_moving3_list2 = [0]

    for i in range(0, len(seafloor_moving3_list) - 1):
        seafloor_moving3_list2.append(seafloor_moving3_list[i])

    #Convert the list to arrays for easy subtraction.
    array1 = np.array(seafloor_moving3_list)
    array2 = np.array(seafloor_moving3_list2)

    #Subtract the arrays
    diffnum_array = np.subtract(array1, array2)

    #Reset the first value to Null
    diffnum_array[0] = 0

    #Count increases
    #Initalize
    increased = 0
    decreased = 0

    for x in diffnum_array:
        if x > 0:
            increased += 1
        if x < 0:
            decreased += 1

    return increased


if __name__ == '__main__':
    print('The three-measurement sliding depth increased {} times'.format(AOC1b('input.txt')))