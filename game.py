import random
from replit import clear
from art import logo
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################




def deal_card():
    """ returns a ransom card """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
   

deal_card()




def compare(user_score, computer_score):
    if user_score == computer_score:
       return "draw"
    elif computer_score == 0:
        return "computer wins"
    elif user_score == 0:
        return "Win with Blackjack"
    elif user_score > 21:
        return " You went over limit and lose"
    elif computer_score > 21 :
        return " Dealer went over you win !"
    elif user_score > computer_score:
        return " you got higher , you win !"
    else:
        return " You lose "

    



def calculate_score(cards):
    """ Takes a list of cards and return the score """
    #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def play_game ():

    print(logo)
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())






   ##The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
   
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards:{user_cards}, current score {user_score} ")
        print(f" Computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
       
            user_should_deal = input(" Do you want another card y or n ?  ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    """Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17. """

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f" Your final hand : {user_cards} final score {user_score}")
    print(f" Computers final hand: {computer_cards}, computers final score: {computer_score}")
    print(compare(user_score, computer_score))



while input(" Do you want to play the game ? Type y or n ? ") == "y":
    clear()
    play_game()
