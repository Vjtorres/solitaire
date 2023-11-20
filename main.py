import random
 
# Define the card suits and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10' 'J', 'Q', 'K', 'A']

# Function that creates the deck
def createDeck():
    deck = [{'value':values, 'suit':suits} for value in values for suit in suits]
    return deck

# Function that shuffles the deck
def shuffleDeck(deck):
    random.shuffle(deck)

# Create and display the game board
def gameBoard(foundation, RSandCS, hand):
    print("\nFoundation:")
    for suit, value in foundation:
        print(f"{value} of {suit}")

    print("\nTableau:")
    for row in RSandCS:
        print(row)

    print("\nHand:", len(hand), "cards remaining")

    