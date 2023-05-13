"""
Created: May 13 15:28:31 2023

by: Rachel Kalusniak
"""

#Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'


#Open txt file and split into list
with open(data_file, 'r') as f:
    input = f.read().splitlines()

#Split into direction and number list
input_edit = [input[x].split(" ", 1) for x in range(0, len(input))]
direct = [i[0] for i in input_edit]
number = [int(i[1]) for i in input_edit]


#Initialize total direction variable
horizontal = 0
depth = 0
aim = 0

#Loop through number and directional lists with new rules to compute total
for i in range(0, len(input_edit)):
    if direct[i] == 'forward':
        horizontal += number[i]
        depth += aim * number[i]
    if direct[i] == 'up':
        aim -= number[i]
    if direct[i] == 'down':
        aim += number[i]

#Compute answer
answer = horizontal * depth


#Print results
print(f'The horizontal position is {horizontal}, and the depth is {depth}.')
print(answer)