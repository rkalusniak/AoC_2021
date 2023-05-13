"""
Created: May 13 12:08:38 2023

by: Rachel Kalusniak
"""
import pandas as pd

test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'


with open(data_file, 'r') as f:
    input = f.read().splitlines()

input_edit = [input[x].split(" ", 1) for x in range(0, len(input))]

direct = [i[0] for i in input_edit]
number = [int(i[1]) for i in input_edit]

directions = pd.DataFrame(data = {'direct': direct, 'number': number})

count = directions.groupby('direct').sum().reset_index()

count.set_index('direct', inplace= True)

down = count.loc['down']['number']
up = count.loc['up']['number']
forward = count.loc['forward']['number']
vertical = down - up
product_directions = vertical * forward

print(count)
print(product_directions)
