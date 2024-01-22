import pyfiglet
import os

# Print header with rules.
def print_header():
    heading_text = pyfiglet.figlet_format("Blackjack")
    print()
    print(heading_text)

    # Print rules
    print("Welcome to python blackjack, basic blackjack rules apply!")
    print("• Dealer will always stand on 17.")
    print("• System will auto pick the value of an ace based on current hand.")
    print("• System deals cards based on a round robin system, one after another.")

# Print the cards and which player they are for.
def print_card(player, cards, _color):
    # Print player name.
    print(color.BOLD + _color + player + color.END)
    # Loop through each card and print with emoji.
    for card in cards:
        print("🃏 " + card)

# Print new empty line.
def print_space():
    print()

# Ask the user for console input.
def ask_input(prompt):
    return input(prompt)

# Clear the current console.
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Formatting for console.
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'