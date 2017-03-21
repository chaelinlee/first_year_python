# Game API
import random
def frest_deck():  
    suits = {"Spade","Heart","Diamond","Club"}
    ranks = {2,3,4,5,6,7,8,9,10,"J","Q","K","A"}
    deck = []
    for a in suits:
        for b in ranks:
            card = {"suits":a, "ranks":b}
            deck.append(card)
    random.shuffle(deck)
    return deck

def hit(deck): 
    if deck == []:
        deck = fresh_deck()
     return deck[0], deck[1:]

def count_score(cards): 
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
            
    while score > 21 and number_of_ace >0:  
        score -=10
        number_of_ace -=1
        
    return score    

def show_cards(cards,message):  
    print(message)             
    for card in cards:         
        print(' ',card['suit'],card['rank'])

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

# Database API

def load_members(): #텍스트 파일에서 한줄씩 읽어서 이름을 키로하는 사전을 만듦
    file = open("members.txt","r")
    members = []
    for line in file:
        name,passwd,tries,wins,chips = line,strip('\n').split(',') 
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members


def store_members(members): #이름을 키로하는 사전 members를 미리 정한 텍스트 파일에 저장함
    file = open ("members.txt","w")
    names = members.keys()
    for name in names:
        passwd,tries,wins,chips = members[name]
        line = name + ','+passwd + ','+ \
               str(tries) + ',' + str(wins)+  ","+\
               str(chips) + '\n'
        file.write(line)
    file.close()

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) >4:
           username = input("Enter your name: (4 letters max) ")
    trypassed = input("Enter your password : ")       
    if username in members.key():
        if trypasswd == members[username][0]:
            tries = members[username][1]
            wins = member[username][2]
            print ("You played",tries,"game and won",wins,"of them.")
            wpercent = 100*(wins/tries) if tries >0 else 0
            print ("Your all- times winning percentage is",\
                   "{0:.1f}".format(wpercent), "%")
            chips = members[3]
            if chips >=0:
                print ("You have",chips,"chips")
            else:
                print("You owe",-chips,"chips")
            return username,tries,wins,chips,members
        else:
            return login(members)
    else:
        members[username] = (trypasswd,0,0,0)
        return username,0,0,0,members 

def show_top5(members): #회원사전 members를 인수로 받아 칩의 보유개수가 가장 많은 순으로
                        #화면에 출력해 주는 프로시저
    print("-----")
    sorted_members =sorted(members.items(),\
                           key=lambda x: x[1][3],reverse= True)\
                           # 칩 개수의 역순으로 정리
    print("All-time Top 5 based on the number of chips earned")
    rank = 1
    for member in sorted_members[:5]:
        chips = member[1][3]
        if chips <= 0:
            break
        print(rank ,".",member[0],":",chips)
        rank += 1

#blackjack
def blackjack():
    print("Welcome to SMaSH Casino!")
    username,tries,wins,chips,members =login(load_members())
    deck= fresh_deck()
    win = 0
    lose = 0
    while True:
        print("-----")
        dealer=[]
        player=[]
        card,deck=hit(deck)
        player.append(card)
        card,deck=hit(deck)
        dealer.append(card)
        card,deck=hit(deck)
        player.append(card)
        card,deck=hit(deck)
        dealer.append(card)

        print("My cards are:")
        print("","****","**")
        print("",dealer[1]["suit"],dealer[1]["rank"])
    
        show_cards(player,"Your cards are:")
        score_player= count_score(player)
        score_dealer= count_score(dealer)

        if score_player==21:
            print("Blackjack! You won!")
            chips +=2
            win +=1
            print ("chips =",chips)
            
        else:
           while score_player <21 and more("Hit? (y/n)"):
               card,deck=hit(deck)
               player.append(card)
               score_player= count_score(player)
               print("",card['suit'],card['rank'])

           if score_player>21:
               print("You Bust! I won.")
               chips -=1
               lose += 1
               print ("chips =",chips)

           if score_player<=21 :
               while score_dealer<= 16:
                   card,deck=hit(deck)
                   dealer.append(card)
                   score_dealer= count_score(dealer)
               show_cards(card,"My cards are")
               
               if score_dealer > 21:
                   print("I Bust! You won.")
                   chips +=1
                   win +=1
                   print ("chips = ",chips)

               elif score_player== score_dealer:
                   print("We draw!")
                   win += 0.5
                   lose += 0.5
          
               elif score_player > score_dealer:
                   print("You Won!")
                   chips +=1
                   win +=1
                   print ("chips=",chips)

               else:
                   print("I won!")
                   chips -=1
                   lose += 1
                   print ("chips=",chips)
                        
        if not more('Play more? (y/n) '):
            break
    print(" -----")
    played = int(win + lose)
    print("You played",played,"games and won",win,"of them")
    wpercent = 100*win/played if played >0 else 0
    print("Your winning percentage today is ",\
          "{0:1f}".format(wpercent), "%")
    tries += played
    wins += win
    members[username] = (members[username][0],tries,wins,chips)
    store_members(members)
    show_top5(members)
    print("Bye!")
      
            
            
    
    

    


    
        

       











    
    
    
