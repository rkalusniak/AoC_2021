"""
Created: May 13 12:08:38 2023

by: Rachel Kalusniak
"""
import pandas as pd

#Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'


#Open txt file and read into list
with open(data_file, 'r') as f:
    input = f.read().splitlines()

#Split list into sub list with direction and number
input_edit = [input[x].split(" ", 1) for x in range(0, len(input))]

direct = [i[0] for i in input_edit]
number = [int(i[1]) for i in input_edit]

#Turn direction and numbers list into pandas dataframe
directions = pd.DataFrame(data = {'direct': direct, 'number': number})

#Group data frame by direction
count = directions.groupby('direct').sum().reset_index()
count.set_index('direct', inplace= True)

#Extract the sum of directions from the group by data frame
down = count.loc['down']['number']
up = count.loc['up']['number']
forward = count.loc['forward']['number']

#Find the net vertical direction and answer
vertical = down - up
product_directions = vertical * forward


#Print the count dataframe and AoC answer
print(count)
print(product_directions)
