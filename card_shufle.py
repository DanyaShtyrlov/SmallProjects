import random
def create_deck():
    global deck
    cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    sings = ["@", "$", "%", "*"]
    deck = []
    for i in range(4):
        for j in range(13):
            deck.append(cards[j] + sings[i])
    return deck

def shufle_deck():
    global deck
    for i in range(len(deck)):
        shufled_card = random.randint(0, len(deck)-1)
        deck[i], deck[shufled_card] = deck[shufled_card], deck[i]
    return deck

create_deck()
print(*shufle_deck())
