import pytest
import random
import string
import session6
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'deck',
    'spades', 
    'club', 
    'hearts',
    'diamond', 
    'jack', 
    'queen',
    'king',
    'ace',
    'poker', 
    'cards', 
    'suits',
    'vals', 
    'lambda', 
    'map',
    'zip', 
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
]

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            print("Didn't find string" + c)
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_create_deck_default():
    deck = session6.get_card_deck_default()
    assert len(deck) == 52, "Number of cards in the deck must be 52. The deck has "
    for s in suits:
        for v in vals:
            assert ([s, v] in deck), "Deck does not contain required card"

def test_create_deck_default_with_valid_args():
    deck = session6.get_card_deck_default(suits, vals)
    assert len(deck) == 52, "Number of cards in the deck must be 52. The deck has "
    for s in suits:
        for v in vals:
            assert ([s, v] in deck), "Deck does not contain required card"

def test_create_deck_default_with_invalid_args():
    with pytest.raises(ValueError):
        deck = session6.get_card_deck_default(vals, suits)

def test_create_deck_using_zip():
    deck = session6.get_card_deck_using_zip()
    assert len(deck) == 52, "Number of cards in the deck must be 52. The deck has "
    for s in suits:
        for v in vals:
            assert ([s, v] in deck), "Deck does not contain required card"

def test_create_deck_using_zip_with_valid_args():
    deck = session6.get_card_deck_using_zip(suits, vals)
    assert len(deck) == 52, "Number of cards in the deck must be 52. The deck has "
    for s in suits:
        for v in vals:
            assert ([s, v] in deck), "Deck does not contain required card"

def test_create_deck_using_zip_with_invalid_args():
    with pytest.raises(ValueError):
        deck = session6.get_card_deck_using_zip(vals, suits)

def test_create_deck_using_zip_vs_default():
    deck1 = session6.get_card_deck_using_zip(suits, vals)
    deck2 = session6.get_card_deck_default(suits, vals)
    assert (deck1 == deck2), "Decks obtained from normal implementation and from using_zip implementation do not match"

def test_get_random_cards_from_deck_valid():
    deck = session6.get_card_deck_using_zip(suits, vals)
    player = session6.get_random_cards_from_deck(deck, 3)
    assert len(player) == 3, "The number of cards obtained do not match requested number of cards"
    player = session6.get_random_cards_from_deck(deck, 4)
    assert len(player) == 4, "The number of cards obtained do not match requested number of cards"
    player = session6.get_random_cards_from_deck(deck, 5)
    assert len(player) == 5, "The number of cards obtained do not match requested number of cards"
    for i in range(0, len(player)):
        for j in range(i+1, len(player)):
            assert player[i] != player[j], "Same player got the same card twice"

    
def test_get_random_cards_from_deck_invalid():
    deck = session6.get_card_deck_using_zip(suits, vals)
    with pytest.raises(ValueError):
        player = session6.get_random_cards_from_deck(deck, 2)
  
    with pytest.raises(ValueError):
        player = session6.get_random_cards_from_deck(deck, 6)
    
def test_royal_flush():
    deck = session6.get_card_deck_using_zip(suits, vals)
    filtered_deck = list(filter(lambda x: x[1] in ['ace', 'king', 'queen', 'jack', '10'], deck))
    kind = random.sample(suits, 4)
    filtered_deck = list(filter(lambda x: x[0] == kind[1], filtered_deck))
    player1 = session6.get_random_cards_from_deck(filtered_deck, 5)
    remaining_deck = [item for item in deck if item not in player1]
    player2 = session6.get_random_cards_from_deck(remaining_deck, 5)
    assert session6.check_royal_flush(player1) == True, "Failed to check royal flush"

def test_straight_flush():
    #TODO
    assert False, "TODO TEST"

def test_four_of_a_kind():
    #TODO
    assert False, "TODO TEST"

def test_full_house():
    deck = session6.get_card_deck_using_zip(suits, vals)
    ranks = random.sample(vals, 2)
    ranks1 = list(filter(lambda x: x[1] == ranks[0], deck))
    ranks2 = list(filter(lambda x: x[1] == ranks[1], deck))
    player1 = session6.get_random_cards_from_deck(ranks1, 3)
    player2 = session6.get_random_cards_from_deck(ranks2, 3)
    for card in player2:
        player1.append(card)
    player1 = random.sample(player1, 5)
    remaining_deck = [item for item in deck if item not in player1]
    player2 = session6.get_random_cards_from_deck(remaining_deck, 5)
    assert session6.check_full_house(player1) == True, "Failed to check full house"
    #assert session6.check_poker_winner(player1, player2) == player1, "Failed to check Royal flush"   
    #assert session6.check_poker_winner(player2, player1) == player1, "Failed to check Royal flush"   

def test_flush():
    deck = session6.get_card_deck_using_zip(suits, vals)
    kind = random.sample(suits, 4)
    filtered_deck = list(filter(lambda x: x[0] == kind[1], deck))
    player1 = session6.get_random_cards_from_deck(filtered_deck, 5)
    remaining_deck = [item for item in deck if item not in player1]
    player2 = session6.get_random_cards_from_deck(remaining_deck, 5)
    assert session6.check_flush(player1) == True, "Failed to check flush"

def test_straight():
    #TODO
    assert False, "TODO TEST"

def test_three_of_a_kind():
    #TODO
    assert False, "TODO TEST"

def test_two_pair():
    #TODO
    assert False, "TODO TEST"

def test_one_pair():
    #TODO
    assert False, "TODO TEST"

def test_high_card():
    #TODO
    assert False, "TODO TEST"
