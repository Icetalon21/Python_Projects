'''
cardcountvalue.py
Name: Emilia Huerta
Collaborators:
Date: 9/9/2019
Description: This program takes user input of a card value and prints
the card counting number for that card.
'''


# MIT card counting values:
#
#    2 - 6 should add one to the count, so their value is 1
#    7 - 9 have no effect on the count, so their value is 0
#    A, 10, J, Q, and K should subtract one from the count,
# so their value is -1



# this is a list containing all of the valid values for a card
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
count = 0
# Write some code that takes a card as input (remember to
# check it for validity) and outputs the MIT card counting
# value of that card. Use multiple if/else statements
# to determine the card counting value of the user's input.
EnterCardValue = input("Enter Card Value : ")

if (EnterCardValue not in cards):
    print("not valid")

if (EnterCardValue in cards):
    print("valid")

if (EnterCardValue in ('2','3','4','5','6')):
    print("Add one to the count. The count is: ", count + 1)


if (EnterCardValue in ('7','8','9')):
    print("has no effect on the count. The count is: ", count + 0)

if (EnterCardValue in ('A','10','J', 'Q', 'K')):
    print("Subtract one from the count. The count is: ", count -1)


# (hint: reuse some of your code from cardlist.py)
