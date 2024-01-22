from sys import exit
import random
import utils
import pyfiglet
from config import *

# Cards the player has been delt.
player_cards = []

# Dealer cards.
dealer_cards = []

# Deal cards to the players, in a round robin.
def deal(turn):
    # Pick a random card for this deal.
    card = random.choice(cards)

    if (turn == "player"):
        player_cards.append(card)

        if (len(dealer_cards) <= 1):
            deal("dealer")
            
    
    if (turn == "dealer"):
        dealer_cards.append(card)

        # Deal the player cards, until they have two.
        if (len(player_cards) <= 1):
            deal("player")

# Add new random card to player.
def hit(_cards):
    card = random.choice(cards)
    _cards.append(card)

# Count value of players cards.
def count_cards(cards):
    current_count = 0
    num_of_aces = 0

    # Loop through each card and count it.
    for card in cards:
        value = card_dict[card]

        # Skip card if it is ace.
        if (card == "Ace"):
            num_of_aces = num_of_aces + 1
        else:
            # Add current card to card value.
            current_count = current_count + value

    # If the player has an ace
    if (num_of_aces > 0):
        for ace in range(num_of_aces):
            # if ace was used as 11 and would be over 21, use as 1.
            if ((current_count + 11) > 21):
                current_count = current_count + 1
            # Using as 11 since it wouldn't bust card set. 
            else:
                current_count = current_count + 11

    return current_count

# Check if a player has bust.
def check_for_bust(cards):
    count = count_cards(cards)

    if (count > 21):
        return True
    else:
        return False

# Simulate dealer with stand at 17.
def simulate_dealer():
    utils.clear()

    # Handle printing header and cards.
    utils.print_header()
    print_hands()

    # Count the cards.
    count = count_cards(dealer_cards)

    if (count > 21):
        return

    if (count == 21):
        return

    # Dealer is under 16 cards.
    if (count <= 16):
        hit(dealer_cards)
        simulate_dealer()

# Prompt user with menu and game.
def prompt_user():
    utils.clear()

    # Handle printing header and cards.
    utils.print_header()
    print_hands()

    # Prompt user for input.
    utils.print_space()
    action = utils.ask_input("Would you like to hit or stand?: ")

    # User stand, move to dealer.
    if (action == "stand"):
        simulate_dealer()

    # User hits, deal next card.
    if (action == "hit"):
        hit(player_cards)
        
        # Player bust, with hit.
        if (check_for_bust(player_cards)):
            return

        if (count_cards(player_cards) == 21):
            simulate_dealer()
            return
        
        prompt_user()
    
# Print the cards to the console.
def print_hands():
    # Print the players cards.
    utils.print_space()
    utils.print_card("Your Hand", player_cards, utils.color.PURPLE)
    print(count_cards(player_cards))

    # Print the players cards.
    utils.print_space()
    utils.print_card("Dealer Hand", dealer_cards, utils.color.GREEN)
    print(count_cards(dealer_cards))

# Prompt user to play again.
def play_again():
    utils.print_space()
    play_again = utils.ask_input("Play Again? (yes or no): ")
    if (play_again.lower() == "yes" or play_again.lower() == "y"):
        player_cards.clear()
        dealer_cards.clear()
        main()

    if (play_again.lower() == "no" or play_again.lower() == "n"):
        exit()

# Main
def main():

    deal("player")
    prompt_user()

    player_count = count_cards(player_cards)
    dealer_count = count_cards(dealer_cards)

    utils.clear()

    # Both players hit 21.
    if (player_count == dealer_count):
        print(pyfiglet.figlet_format("It's a Tie!"))
        print_hands()
        play_again()
        return
    
    # Both players are over 21.
    if (player_count > 21 and dealer_count > 21):
        print(pyfiglet.figlet_format("Everyone Bust"))
        print_hands()
        play_again()
        return

    # Player is over 21.
    if (player_count > 21):
        print(pyfiglet.figlet_format("You Bust 💣"))
        print_hands()
        play_again()
        return
    
    # Dealer is over 21.
    if (dealer_count > 21):
        print(pyfiglet.figlet_format("Dealer Bust 💣"))
        print_hands()
        play_again()
        return
    
    # Player won with higher hand.
    if (player_count > dealer_count):
        print(pyfiglet.figlet_format("You Won"))
        print_hands()
        play_again()
        return
    
    # Dealer won with higher hand.
    if (player_count < dealer_count):
        print(pyfiglet.figlet_format("Dealer Won"))
        print_hands()
        play_again()
        return
    


main()