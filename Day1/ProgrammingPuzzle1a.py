"""
Created on Mon Jun 8 19:15:03 2023

@author: Rachel Kalusniak
"""

import numpy as np



#Create a function to find the  step direction of a list
def AOC1a(deapthfile):
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


    #Find the number of items in the seafloor list allowing for variability
    length = len(seafloor_list)

   #Initallize an secondary list with the previous value in the same position.
        #The first value is zero becuase there is no previous value.
    seafloor_list2 = [0]

    #Create the secondary list with the previous value in the same position.
    for i in range(0, length - 1):
        seafloor_list2.append(seafloor_list[i])

    #Convert the list to arrays for easy subtraction.
    array1 = np.array(seafloor_list)
    array2 = np.array(seafloor_list2)

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

    #Return the number of the depth measurement increases
    return increased


#Run the Python script above and print results
if __name__ == '__main__':
    print('The depth measurement increased {} times'.format(AOC1a('input.txt')))
