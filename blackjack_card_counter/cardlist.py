'''
cardlist.py
Name: Emilia Huerta
Collaborators:
Date: 9/9/2019
Description: This program checks user input against a list to see if it is valid.
'''


# this is a list containing all of the valid values for a card
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']



# Write some code that prompts the user to enter a
EnterCardValue = input("Enter Card Value : ")


# card value and then checks if it is valid or
# not.
if (EnterCardValue not in cards):
        print("not valid")

if (EnterCardValue in cards):
        print("valid")

#Print a message saying whether
# or not the card is valid.

# (hint: think about what operator you would use
# to see if a value is in a list)
