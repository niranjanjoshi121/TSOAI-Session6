# Session-6 assignment: 
## Poker - the game of cards

## Problem statement
### This assignment consists of writing functions to create a deck of cards, draw cards from the deck and then test differnt winning scenarios in the game of poker. 

#### Specifically, the assignment includes

* Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
* Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
* Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker.

#### The following lists are used to represent values and suits of the cards in the deck.
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
#### The following functions are includes

* get_card_deck_default(kind_list = suits, value_list = vals):
* get_card_deck_using_zip(kind_list=suits, value_list=vals):
* get_random_cards_from_deck(deck, num_cards):
* check_royal_flush(cards):
* check_straight_flush(cards):
* check_four_of_a_kind(cards):
* check_full_house(cards):
* check_flush(cards):
* check_straight(cards):
* check_three_of_a_kind(cards):
* check_two_pairs(cards):
* check_on_pair(cards):
* check_high_card(cards):
* check_poker_winner(player1, player2):

### The following tests are used to validate the functions above:
* test_readme_exists() - Checks if this file i.e. README.md exists or not
* test_readme_contents() - Checks if this file i.e. README.md contains more than 500 words.
* test_readme_proper_description() - Checks if this file i.e. README.md has valid contents by checking against a set of relevant keywords     (e.g. function names used in session4.py) 
* test_readme_file_for_formatting() - Checks if this file i.e. README.md has appropriate formatting.
* test_indentations() - Checks if the indentation is correct or not by ensuring the number of spaces in the code is a multiple of 4.
* test_function_name_had_cap_letter() - Checks if the function names has a capital letter in it or not.
* test_create_deck_default() - Checks if the deck created using default method with default values is correct of not.
* test_create_deck_default_with_valid_args() - Checks if the deck created using default method with valid args is correct or not.
* test_create_deck_default_with_invalid_args() - Checks if the deck created using default method with invalid args raises value error or not.
* test_create_deck_using_zip() - Checks if the deck created using zip method with default args is correct or not.
* test_create_deck_using_zip_with_valid_args() - Checks if the deck created using zip with valid args is correct or not.
* test_create_deck_using_zip_with_invalid_args() - Checks if the deck created using zip with invalid args raises appropriate value error or not
* test_create_deck_using_zip_vs_default() - Checks if the deck created using zip is same as the deck created using default method or not.
* test_get_random_cards_from_deck_valid() - Checks if the cards drawn from the deck using valid args.
* test_get_random_cards_from_deck_invalid() - Checks if drawing cards from deck using invalid args raises value error or not.
* test_royal_flush() - Checks if the given set of cards form a royal flush.
* test_straight_flush() - Checks if the given set of cards form a straight flush.
* test_four_of_a_kind_flush() - Checks if the given set of cards form a four_of_a_kind.
* test_full_house() - Checks if the given set of cards form a full house.
* test_flush() - Checks if the given set of cards form a flush.
* test_straight() - Checks if the given set of cards form a straight.
* test_three_of_a_kind() - Checks if the given set of cards form three of a kind
* test_two_pair() - Checks if the given set of cards form two-pair
* test_one_pair() - Checks if the given set of cards form one-pair
* test_high_card() - Checks if the given set of cards form high card

