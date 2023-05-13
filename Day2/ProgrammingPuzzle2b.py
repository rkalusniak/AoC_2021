"""
Created: May 13 15:28:31 2023

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

horizontal = 0
depth = 0
aim = 0
for i in range(0, len(input_edit)):
    if direct[i] == 'forward':
        horizontal += number[i]
        depth += aim * number[i]
    if direct[i] == 'up':
        aim -= number[i]
    if direct[i] == 'down':
        aim += number[i]

answer = horizontal * depth

print(f'The horizontal position is {horizontal}, and the depth is {depth}.')
print(answer)