"""
Created: May 13 22:49:17 2023

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

#We are creating a list called bingo cards that has each card as an array in the list.
bingo_cards = []
for i in range(0, num_cards):
        bingo_cards.append(np.array(bingo_rows[(i*5): (i*5)+5]))



#We need to combine the rows and columns into 1 large list
check_groups = []
for i in range(0, len(bingo_cards)):
    for x in bingo_rows[i*5:(i*5)+5]:
        check_groups.append(x)
    for y in bingo_columns[i*5:(i*5)+5]:
        check_groups.append(y)

#Now break the list into sub lists by card
check_groups_bycard = []
for i in range(0, len(bingo_cards)):
    check_groups_bycard.append(check_groups[i*10:i*10+10])


#Now we can start testing to see if the calls match the bingo cards
#Loop through list by card and find the call number when each card wins
    #Start with looping through the cards
    #We can start a call list 4 becuase we are not going to get a match if we call less than 5 numbers.
    #We check until all the items against our groups list. Check returns true.
    #Then we break the inner loop then we break the outer loop.
    #We record the call number for the final calulation.
matches = []
for h in range(0, len(bingo_cards)):
    for i in range(4, len(call_list)):
        for j in range(10):
            check = all(item in call_list[0:i] for item in check_groups_bycard[h][j])
            if check:
                matches.append(i)
                break
        if check:
            break


#Now we need to find the largest call number that matches.
#Subtract 1 from the minimum because the list is 1 ahead of the last value
max_call_num = matches[matches.index(max(matches))]

#Turn the minimum index into the minimum value
last_call_num = call_list[max_call_num - 1]

#Now we need to find which card matched.
match_card = matches.index(max(matches))


#Now we need to sum the non-matched values on the matched card.
#We are pulling back out that list of arrays for each bingo card to do this.
    #This why matched card above needs to be zero indexing
#We convert the matched card and called numbers to 1D arrays, so we can find the difference to sum
match_card_1d = bingo_cards[match_card].flatten()
final_call_array = np.array(call_list[0:max_call_num])
print(call_list[0:max_call_num])
uncalled_sum = np.setdiff1d(match_card_1d, final_call_array).sum()

#The answer is the sum of the last called number and the unmatched numbers
answer = uncalled_sum * last_call_num

#Print answers
print(f'The last number called is {last_call_num}. The matching card is {match_card}.')
print(f'The sum of uncalled number on that card is {uncalled_sum}. The answer is {answer}.')

