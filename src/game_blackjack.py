"""
############### Our Blackjack House Rules #####################
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The the Ace can count as 11 or 1.
The cards have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""

import os
import random

LOGO = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# functions
clear = lambda: os.system("clear")


def receive_cards(amount):
    DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = []
    for x in range(amount):
        cards.append(random.choice(DECK))
    return cards


def sum_cards(cards):
    total = 0
    for card in cards:
        total += card
    return total


def print_standings(msg):
    clear()
    print(LOGO)
    print(msg)
    print(f"Dealer:\t[{dealer_cards[0]}, ?]")
    print(f"You:\t{player_cards}")


def print_result(msg):
    clear()
    print(LOGO)
    print(f"Dealer:\t{dealer_cards}")
    print(f"You:\t{player_cards}")
    print(msg)


run = True

while run == True:

    # variables
    player_hit = True
    dealer_hit = True

    player_cards = receive_cards(2)
    dealer_cards = receive_cards(2)
    player_score = sum_cards(player_cards)
    dealer_score = sum_cards(dealer_cards)

    if player_score == 22:
        player_cards[player_cards.index(11)] = 1
    if dealer_score == 22:
        dealer_cards[dealer_cards.index(11)] = 1

    # game start
    print_standings(
        "You and the dealer received each two randomly choosen cards from a fresh deck."
    )

    if player_score == 21 and dealer_score != 21:
        print_result("Player wins the game with Blackjack.")
    elif dealer_score == 21 and player_score != 21:
        print_result("Dealer wins the game with Blackjack.")
    elif dealer_score == 21 and player_score == 21:
        print_result("Draw game. Blackjack for dealer and player.")

    while player_hit is True:
        get_card = input("Stand [s] or hit [h]? ").lower()

        if get_card == "h" or get_card == "hit":

            new_card = receive_cards(1)

            if new_card == 11 and player_score + new_card > 21:
                new_card = 1

            player_cards.extend(new_card)
            player_score = sum_cards(player_cards)

            if player_score > 21:
                player_hit = False
                dealer_hit = False
                print_result("You loose")
            else:
                print_standings(
                    "You received a new randomly choosen cards from the deck."
                )

        elif get_card == "s" or get_card == "stand":
            player_hit = False

    while dealer_hit is True:
        if dealer_score < 17:
            dealer_cards.extend(receive_cards(1))
            dealer_score = sum_cards(dealer_cards)
        else:
            dealer_hit = False

    if player_score <= 21:

        if dealer_score > 21:
            print_result("Player wins the game.")
        elif player_score == dealer_score:
            print_result("Draw!")
        elif player_score > dealer_score:
            print_result("Player wins the game.")
        else:
            print_result("Loose!")

    run_again = input("Run again [y]? ").lower()

    if run_again != "y":
        run = False
