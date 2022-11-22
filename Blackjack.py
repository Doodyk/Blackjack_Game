import random
import time
class Cards:
    instances = []

    def __init__(self, value, symbol, _played):
        self.value = value
        self.symbol = symbol
        self._played = _played
        __class__.instances.append(self)

    def isplayed(self):
        if(self._played == True):
            return True
        else:
            return False
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["♣", "♥", "♠", "♦"]:
             for value in range(1, 14):
                self.cards.append(Cards(value, suit, False))
                #print(value, suit)
    
deck = Deck()

def drawacard():
    while True:
        randomIndex = random.randrange(len(Cards.instances))
        randCard = Cards.instances[randomIndex]
        if(randCard._played == False):
            data = str(randCard.value)+" "+str(randCard.symbol)
            return(data)

def DisplayCards(Cards,id):
    if(id == 0):
        for i in range(0,len(Cards)):
            first_char = str(Cards[i])[0:2]
            if(first_char == '1 '):
                print("A", str(Cards[i])[-1])
            elif(first_char == '11'):
                print("J", str(Cards[i])[-1])
            elif(first_char == '12'):
                print("Q", str(Cards[i])[-1])
            elif(first_char == '13'):
                print("K", str(Cards[i])[-1])
            else:
                print(Cards[i])
    else:
        first_char = Cards[:2]
        if(first_char == '1 '):
            print("A", Cards[-1])
        elif(first_char == '11'):
            print("J", Cards[-1])
        elif(first_char == '12'):
            print("Q", Cards[-1])
        elif(first_char == '13'):
            print("K", Cards[-1])
        else:
            print(Cards)


def PlayGame():
    PlayerCards = []
    while len(PlayerCards) != 2:
        PlayerCards.append(drawacard())
    print("Your Cards")
    DisplayCards(PlayerCards,0)

    DealerCards = []
    while len(DealerCards) != 2:
        DealerCards.append(drawacard())
    print("Dealers Card")
    DisplayCards(DealerCards[1],1)
    print()
    print()
    while True:
        DisplayCards(PlayerCards,0)
        PlayerTotal = 0
        PlayerAce = False
        for i in PlayerCards:
            if (int(i[0:2]) == 1):
                if(PlayerTotal <= 10):
                    PlayerTotal += 11
                    PlayerAce = True
            else:
                PlayerTotal += int(i[0:2])
        time.sleep(1)
        if(PlayerTotal > 21 and PlayerAce):
            PlayerTotal -= 10
        print("Cards total to: ",PlayerTotal)
        if(PlayerTotal > 21):
            print("busted at ", PlayerTotal)
            break
        elif(PlayerTotal == 21):
            print("BlackJack!")
            break
        else:
            print("Draw of Stand?")
            inputData = input()
            if(inputData.lower() == "draw"):
                PlayerCards.append(drawacard())
            elif(inputData.lower() == "stand"):
                print("You Stand Your Ground")
                break
    print("Dealers Card")
    DisplayCards(DealerCards,0)
    while True:
        DealerCardtotal = 0
        DealerAce = False
        for i in DealerCards:
            if (int(i[0:2]) == 1):
                if(DealerCardtotal <= 10):
                    DealerCardtotal += 11
                    DealerAce = True
            else:
                DealerCardtotal += int(i[0:2])
        if(DealerCardtotal > 21 and DealerAce):
            DealerCardtotal -= 10
        print(DealerCardtotal)
        if(DealerCardtotal >= 17 and DealerCardtotal < 22):
            print("Dealer Stands at", DisplayCards(DealerCards))
            if(DealerCardtotal < PlayerTotal and PlayerTotal <= 21):
                VictoryScreen()
            else:
                DefeatScreen()
            break
        elif(DealerCardtotal == 21):
            print("Dealer Lands BlackJack!")
            DefeatScreen()
            break
        elif(DealerCardtotal > 21):
            print("Dealer Has Gone Bust")
            if(PlayerTotal < 22):
                VictoryScreen()
            else:
                DefeatScreen()
            break
        else:
            DealerCards.append(drawacard())
            DisplayCards(DealerCards,0)
    
def VictoryScreen():
    print("Congrats on winnings")

def DefeatScreen():
    print("Unlucky, better luck next time")

def ResetGame():
    globals()[deck] = Deck()

def main():
    print("Loaded Standard 52 card deck")
    while True:
        PlayGame()
        ResetGame()

if __name__ == "__main__":
    main()
    





