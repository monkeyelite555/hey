import random
suits=["of Spades","of Hearts","of Diamonds","of Clubs"]
ranks=['2','3','4','5','6','7','8','9','10','Jack','Queen','King',"Ace"]
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playerHand={}
dealerHand={}
playerValue=0
dealerValue=0
active=0

def draw_card(drawer):
    while True:
        card=''
        rank=random.choice(ranks)
        card+=rank
        card+=' '
        card+=random.choice(suits)
        if card not in playerHand.keys() and card not in dealerHand.keys():
            drawer[card]=values[rank]
            if active==1:
                print("The",card,"was drawn.")
            break
        else:
            card=''

def valueCheck(hand):
    return sum(hand.values())

def gameplay():
    active=0
    playerHand={}
    dealerHand={}
    for i in range(2):
        draw_card(playerHand)
        draw_card(dealerHand)
    active=1
    while active==1:
        print("Your hand:",playerHand)
        print("Total:",valueCheck(playerHand))
        if valueCheck(playerHand)>21:
            print("Player busts!")
            break
        if input("Hit or stand? (H/S) ").lower()=='h':
            draw_card(playerHand)
        else:
            print("Player stands!")
            break
    active=0
    while valueCheck(dealerHand)<17:
        draw_card(dealerHand)
    print("Dealer's hand:",dealerHand)
    print("Total:",valueCheck(dealerHand))
    if valueCheck(dealerHand)>21:
        print("Dealer busts!")
    if valueCheck(dealerHand)==valueCheck(playerHand):
        print("It's a tie!")
    elif valueCheck(dealerHand)>21 and valueCheck(playerHand)>21:
        if valueCheck(playerHand)-21<valueCheck(dealerHand)-21:
            print("Player wins!")
        else:
            print("Dealer wins!")
    elif valueCheck(playerHand)>21 and valueCheck(dealerHand)<=21:
        print("Dealer wins!")
    elif valueCheck(playerHand)<=21 and valueCheck(dealerHand)>21:
        print("Player wins!")
    elif 21-valueCheck(playerHand)<21-valueCheck(dealerHand):
        print("Player wins!")
    else:
        print("Dealer wins!")

gameplay()
while True:
    if input("Play again? (Y/N) ").lower()=='y':
        gameplay()
    else:
        break

        
