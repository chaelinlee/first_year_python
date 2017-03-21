
import random
def frest_deck():  #카드 1벌을 무작위로 섞어서 내주는 함수
    suits = {"Spade","Heart","Diamond","Club"}
    ranks = {2,3,4,5,6,7,8,9,10,"J","Q","K","A"}
    deck = []
    for a in suits:
        for b in ranks:
            card = {"suits":a, "ranks":b}
            deck.append(card)
    random.shuffle(deck)
    return deck

def hit(deck): #카드 리스트 deck을 인수로 받아 맨 앞의 카드 1장과
               #나머지 deck을 쌍으로 내주는 함수 
    if deck == []:
        deck = fresh_deck()
     return deck[0], deck[1:] #실행창에서 할때 c,d=hit(d)라고 하게 되면
                              #c에는 deck의 맨 앞의 카드가 오고 
                              #d에서는 그것을 제외한 모든 카드가 온다.  

    

def count_score(cards): #카드 리스트 cards를 인수로 받아 카드 점수의 합을 내주는 함수 
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card['rank'] 
        if rank == 'A':
            score +=11
            number_of_ace +=1
        elif rank in {"J","Q","K"}:
            score +=10
        else:
            score +=rank
            
    while score > 21 and number_of_ace >0: #if가 아닌 이유는 에이스가 2개 있을수도 있으니까 
        score -=10
        number_of_ace -=1
        
    return score    

def show_cards(cards,message): #카드 리스트 cards와 문자열 메세지를 인수로 받아 
    print(message)             #메세지를 먼저 프린드 한뒤 
    for card in cards:         # 한줄에 카드 한장씩 모두 프린트하는 함수 
        print(' ',card['suit'],card['rank'])

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

    # 위에 있는 return을 사실 if answer=='y' return True else:return False와 동일하다. 




    
