import random


def shuffle_cards(cards):
    rand_values = set()
    shuffled_cards = []
    while len(cards) != len(rand_values):
        curr_rand = random.randrange(0, len(cards))
        while curr_rand in rand_values:
            curr_rand = random.randrange(0, len(cards))
        shuffled_cards.append(curr_rand)
        rand_values.add(curr_rand)
    return shuffled_cards


print(shuffle_cards(list(range(5))))
