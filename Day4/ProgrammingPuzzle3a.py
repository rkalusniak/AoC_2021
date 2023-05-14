"""
Created: May 13 4:38:17 2023

by: Rachel Kalusniak
"""
import re
import numpy as np

#Allow to run with test or actual file
test = False
if test:
    data_file = 'input_test.txt'
else:
    data_file = 'input.txt'


#Open txt file and numbers called (zero line) into list
with open(data_file, 'r') as f:
    #Reading in just the string (item 0 of list) to do further manipulation later
    call = f.readlines()[0:1][0]

#Remove extra lines and break into integer list on the commas
call_list = call.rstrip().rsplit(",")
call_list = [int(i) for i in call_list]


#Open txt file and read in bingo cards (doesn't like doing two at once so need separate with statement)
with open(data_file, 'r') as f:
    # Reading from second line (after call) onward
    bingo_data = f.readlines()[2:]

#Let's reformat the bingo data into something usable
#Strip the new line characters
bingo_data = [i.strip() for i in bingo_data]

#Use regex to convert string to individual list values. Posibility for double spaces, so I used the + indivcator
bingo_data = [re.split('\s+', i) for i in bingo_data]

#Get rid of the empty list values. We don't need an indicator since we know each card is 5 by 5
#While we have the list broken by recursive list, use  list comprehension to change from string to integer
bingo_rows = []
for i in range(0, len(bingo_data)):
    if len(bingo_data[i]) > 1:
        bingo_rows.append([int(j) for j in bingo_data[i]])

num_cards = int(len(bingo_rows) / 5)

#i tells it to loop through each card
#j tells it to loop through all 5 columns in a card
#k tells it to loop through the 5 rows in a card
bingo_columns = []
for i in range(0, num_cards):
    for j in range(5):
        for k in range(5):
            bingo_columns.append(bingo_rows[i*5+k][j])

#The bingo_columns above gives 1 long list. This breaks it into sub list of length 5 for each column separately
bingo_columns = [bingo_columns[x:x+5] for x in range(0, len(bingo_columns), 5)]

#Let's find the diagonals
#We are creating a list called bingo cards that has each card as an array in the list.
bingo_cards = []
for i in range(0, num_cards):
        bingo_cards.append(np.array(bingo_rows[(i*5): (i*5)+5]))

#Now we can find to diagonals as a list. To find the downward diagonals we need to flip the array
bingo_diag = [list(np.diagonal(bingo_cards[i])) for i in range(num_cards)]
bingo_flipdiag = [list(np.fliplr(bingo_cards[i]).diagonal()) for i in range(num_cards)]



#Not we can start testing to see if the calls match the bingo cards
#We are going to check when each set of lines (rows, columns, diagonals, and flipped diagonals matches)


#First we need to initialize to an obviously large value, so we don't get an error if there is no match.
    #Rows and columns are equal, so it doesn't matter which one we use.
        #There are fewer diagonals, so that is a bad option
row_call_num = len(bingo_rows) * 1000
col_call_num = len(bingo_rows) * 1000
diag_call_num = len(bingo_rows) * 1000
flipdiag_call_num = len(bingo_rows) * 1000
row = len(bingo_rows) * 1000
column = len(bingo_rows) * 1000
diag = len(bingo_rows) * 1000
flipdiag = len(bingo_rows) * 1000


#Loop through the rows
    #We can start a call list 4 becuase we are not going to get a match if we call less than 5 numbers.
    #We check until all the items in the call list are in bingo row j. Check_rows returns true.
    #Then we break the inner loop then we break the outer loop.
    #We record the winning row number and call number for the final calulation.
for i in range(4, len(call_list)):
    for j in range(0, len(bingo_rows)):
        check_rows = all(item in call_list[0:i] for item in bingo_rows[j])
        if check_rows:
            row = j
            row_call_num = i
            break
    if check_rows:
        break

#Loop through columns with same method as rows.
for i in range(4, len(call_list)):
    for k in range(0, len(bingo_columns)):
        check_columns = all(item in call_list[0:i] for item in bingo_columns[k])
        if check_columns:
            column = k
            col_call_num = i
            break
    if check_columns:
        break

#Loop through diagonals with same method.
for i in range(4, len(call_list)):
    for l in range(0, len(bingo_diag)):
        check_diag = all(item in call_list[0:i] for item in bingo_diag[l])
        if check_diag:
            diag = l
            diag_call_num = i
        break
    if check_diag:
        break

#Looped through flipped diagonals with same method
for i in range(4, len(call_list)):
    for m in range(0, len(bingo_flipdiag)):
        check_flipdiag = all(item in call_list[0:i] for item in bingo_flipdiag[m])
        if check_flipdiag:
            flipdiag = m
            flipdiag_call_num = i
        break
    if check_flipdiag:
        break

print(f'Call Numbers - rows: {row_call_num}, columns: {col_call_num}, diag: {diag_call_num}, flipdiag: {flipdiag_call_num}')


#Now we need to find the smallest call number that matches.
    #We need to put the values in list to pull the minimum value
#Subtract 1 from the minimum because the list is 1 ahead of the last value
matches = (row_call_num, col_call_num, diag_call_num, flipdiag_call_num)
min_call_num = matches[matches.index(min(matches))]

#Turn the minimum index into the minimum value
last_call_num = call_list[min_call_num - 1]

#Now we need to find which card matched.
#We have to check all dimensions to see which one had the minimum call number
    #The matching card uses zero indexing
if min_call_num == row_call_num:
    match_card = int((row + 1)/5)
elif min_call_num == col_call_num:
    match_card = int((column + 1)/5)
elif min_call_num == diag_call_num:
    match_card = diag
elif min_call_num == flipdiag_call_num:
    match_card = flipdiag

#Now we need to sum the non-matched values on the matched card.
#We are pulling back out that list of arrays for each bingo card to do this.
    #This why matched card above needs to be zero indexing
#We convert the matched card and called numbers to 1D arrays, so we can find the difference to sum
match_card_1d = bingo_cards[match_card].flatten()
final_call_array = np.array(call_list[0:min_call_num])

uncalled_sum = np.setdiff1d(match_card_1d, final_call_array).sum()

#The answer is the sum of the last called number and the unmatched numbers
answer = uncalled_sum * last_call_num

#Print answers
print(f'The last number called is {last_call_num}. The matching card is {match_card}.')
print(f'The sum of uncalled number on that card is {uncalled_sum}. The answer is {answer}.')