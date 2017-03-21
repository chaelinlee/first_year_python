import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2,3,4,5,6,7,8,9,10,"J","Q","K","A"}
    deck=[]
    for a in suits:
        for b in ranks:
            card={"suit":a, "rank":b}
            deck.append(card)
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck ==[]:
        deck = fresh_deck()
    return deck[0],deck[1:]

def count_score(cards):
    score=0
    for card in cards:
        rank= card['rank']
        if rank== "A":
            score +=11
            number_of_ace +=1
        elif rank in {"J","Q","K"}:
            score +=10
        else:
            score +=rank
    while score > 21 and number_of_ace >0:
        score -=10
        number_of_ace -=1
    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        print(' ',card['suit'],card['rank'])


def more(message):
    answer= input(message)
    while not (answer== 'y' or answer== 'n'):
        answer=input(message)
    return asnwer=='y'   

        
