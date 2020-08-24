import random
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def get_card_deck_default(kind_list=suits, value_list=vals):
    if len(kind_list) != 4:
        raise ValueError("kind_list must have exactly 4 entries")
    if len(value_list) != 13:
        raise ValueError("value_list must have exactly 13 entries")
    if kind_list != suits :
        raise ValueError("kind_list does not meet expectation")
    if value_list != vals:
        raise ValueError("value_list does not meet expectation")

    deck = []
    for k in kind_list:
        for v in value_list:
            deck.append([k, v])
    return deck

def get_card_deck_using_zip(kind_list=suits, value_list=vals):
    if len(kind_list) != 4:
        raise ValueError("kind_list must have exactly 4 entries")
    if len(value_list) != 13:
        raise ValueError("value_list must have exactly 13 entries")
    if kind_list != suits :
        raise ValueError("kind_list does not meet expectation")
    if value_list != vals:
        raise ValueError("value_list does not meet expectation")

    return list([x,*y] for x,y in zip(kind_list, value_list) for y in zip(value_list))

def get_random_cards_from_deck(deck, num_cards):
    if num_cards < 3 or num_cards > 5:
        raise ValueError("Can not draw less than 3 or more than 5 cards at a time")
    cards = random.sample(deck, num_cards)
    return cards

def check_royal_flush(cards):
    if len(cards) != 5:
        return False
    unexpected_values = list(filter(lambda x: x[1] not in ['ace', 'king', 'queen', 'jack', '10'], cards))
    print(unexpected_values)
    if (len(unexpected_values) !=0):
        print("Cards contain values < 10")
        return False
    different_color = list(filter(lambda x: x[0] != cards[0][0], cards))
    print(different_color)
    if (len(different_color) != 0):
        print("Cards contain different colors")
        return False
    return True

def check_straight_flush(cards):
    # TODO
    return False

def check_four_of_a_kind(cards):
    # TODO
    return False

def check_full_house(cards):
    if len(cards) < 5:
        return False
    maps = []
    for v in vals:
        maps.append(list(filter(lambda x: x[1] == v, cards)))

    non_empty_lists = [item for item in maps if item]
    if len(non_empty_lists) > 2:
        print("Cards of more than two ranks")
        return False
    if (len(non_empty_lists[0]) == 3 and len(non_empty_lists[1]) == 2):
       return True
    if (len(non_empty_lists[1]) == 3 and len(non_empty_lists[0]) == 2):
       return True

def check_flush(cards):
    if len(cards) < 5:
        return False
    different_kind = list(filter(lambda x: x[0] != cards[0][0], cards))
    if (len(different_kind) > 0):
        print("Cards of different kind")
        return False
    return True

def check_straight(cards):
    # TODO
    return False

def check_three_of_a_kind(cards):
    # TODO
    return False

def check_two_pairs(cards):
    # TODO
    return False

def check_on_pair(cards):
    #TODO
    return False

def check_high_card(cards):
    # TODO
    return False

def check_poker_winner(player1, player2):
    if len(player1) < 2 or len(player1) > 5:
        raise ValueError("Player can not have less than 3 or more than 5 cards at a time")
    if len(player2) < 2 or len(player2) > 5:
        raise ValueError("Player can not have less than 3 or more than 5 cards at a time")
    if len(player1) != len(player2):
        raise ValueError("Players can not have differnt number of cards")

    if (check_royal_flush(player1)):
        return player1
    elif(check_royal_flush(player2)):
        return player2
    elif(check_four_of_a_kind(player1)):
        return player1
    elif(check_four_of_a_kind(player2)):
        return player2
    elif(check_full_house(player1)):
        return player1
    elif(check_full_house(player2)):
        return player2
    elif(check_flush(player1)):
        return player1
    elif(check_flush(player2)):
        return player2
    elif(check_straight(player1)):
        return player1
    elif(check_straight(player2)):
        return player2
    elif(check_three_of_a_kind(player1)):
        return player1
    elif(check_three_of_a_kind(player2)):
        return player2
    elif(check_two_pairs(player1)):
        return player1
    elif(check_two_pairs(player2)):
        return player2
    elif(check_one_pair(player1)):
        return player1
    elif(check_one_pair(player2)):
        return player2
    elif(check_high_card(player1)):
        return player1
    elif(check_high_card(player2)):
        return player2
    else:
        return None
