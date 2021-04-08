#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars


import random
from random import shuffle

def give_char_val(charrank):
    allo = ["J", "Q", "K", "A"]
    for items in allo:
        if charrank == items:
            return allo.index(items)

class Deck():
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, cards = [], deckeins = [], deckzwei = []):
        self.cards = cards
        self.deckeins = deckeins
        self.deckzwei = deckzwei

    def deck_creation(self):
        cards = []
        for items in self.SUITE:
            for ranks in self.RANKS:
                onecard = [items + ranks]
                cards = cards + onecard
        self.cards = cards

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def split_deck(self, whichHalf):
        if whichHalf == 2:
            self.deckzwei = self.cards[:26]
        elif whichHalf == 1:
            self.deckeins = self.cards[26:]


class Hand():

    def __init__(self, personaldeck = []):
        self.personaldeck = personaldeck

    def mycard_bigger(self, cardme, cardvs):
        numbs = ["0","1","2","3","4","5","6","7","8","9"]
        persons = ["J", "Q", "K", "A"]
        if cardme[-1] == cardvs[-1]:
            return 100
        elif cardme[-1] in numbs and cardvs[-1] in persons:
            return False
        elif cardme[-1] in persons and cardvs[-1] in numbs:
            return True
        elif cardme[-1] in persons and cardvs[-1] in persons:
            rankme = give_char_val(cardme[-1])
            rankvs = give_char_val(cardvs[-1])
            if rankme > rankvs:
                return True
            elif rankme < rankvs:
                return False
        elif cardme[-1] in numbs and cardvs[-1] in numbs:
            rankme = int(cardme[-1])
            rankvs = int(cardvs[-1])
            if rankme > rankvs:
                return True
            elif rankme < rankvs:
                return False

    def add_card(self, boolbigger, mydeck, vsturned):
        if boolbigger == True:
            for cards in vsturned:
                mydeck.extend(cards)

    def remove_card(self, boolbigger, mydeck, myturned):
        if boolbigger == False:
            for cards in myturned:
                mydeck.remove(cards)

class Player(Hand):

    def __init__(self, name = "Player 1"):
        self.name = name

    def plyr_name(self):
        usrput = raw_input("Please type in your Gametag: ")
        self.name = usrput

    def turnup_card(self, mydeck, drawornot):
        if drawornot == 100:
            return mydeck[:2]
        else:
            pl_choice = 0
            while pl_choice != "Q":
                pl_choice = raw_input("-Input P for turning up the next card\n\
-Input C to check if you still have cards left\n\
-Input Q to Quit the Game ")
                if pl_choice == "C":
                    print("You still have {} cards left in your deck".format(len(mydeck)))
                elif pl_choice == "P":
                    return [mydeck[0]]
                elif pl_choice == "Q":
                    q_n_a = raw_input("Are you sure you want to quit?\n\
-Y for Yes\n-N for No ")
                    if q_n_a == "Y":
                        continue
                    elif q_n_a == "N":
                        pl_choice = 0
                else:
                    print("\nPlease type in a Valid Letter!\n")

    def pc_turnup(self,pcdeck, drawornot):
        if drawornot == 100:
            return pcdeck[:2]
        else:
            return [pcdeck[0]]

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

playerone = Player()
playertwo = Player()
handone= Hand()
handtwo= Hand()

playertwo.plyr_name()

maindeck = Deck()
maindeck.deck_creation()
maindeck.shuffle_deck()
maindeck.split_deck(1)
maindeck.split_deck(2)

playerone.personaldeck = maindeck.deckeins
playertwo.personaldeck = maindeck.deckzwei

print("The personal decks have been intialized! Let's Go!")
ergebnis = ""


while len(playerone.personaldeck) != 0 and len(playertwo.personaldeck) != 0:
    if ergebnis == 100:
        turnedone = turnedone
        turnedtwo = turnedtwo
    else:
        turnedone = []
        turnedtwo = []


    mecard = playertwo.turnup_card(playertwo.personaldeck, ergebnis)
    pccard = playerone.pc_turnup(playerone.personaldeck, ergebnis)
    if ergebnis != 100:
        turnedone += pccard
        turnedtwo += mecard
    print("Your Card: {}".format(mecard[0]))
    print("PC Card: {}".format(pccard[0]))
    ergebnis = handtwo.mycard_bigger(mecard[0], pccard[0])
    if ergebnis == True:
        print("Congratulation! Your Card is bigger, you won this round\n")
    elif ergebnis == False:
        print("Too bad! Your Card is the smaller one, you lost this round\n")
    elif ergebnis == 100:
        print("It's a draw! Now it's time for War!\n")
    ergebnispc = handone.mycard_bigger(pccard[0], mecard[0])
    handtwo.add_card(ergebnis, playertwo.personaldeck, turnedone)
    handtwo.remove_card(ergebnis, playertwo.personaldeck, turnedtwo)
    handone.add_card(ergebnispc, playerone.personaldeck, turnedtwo)
    handone.remove_card(ergebnispc, playerone.personaldeck, turnedone)

if len(playertwo.personaldeck) == 0:
    print("YOU LOST! THE WINNER IS: PC\n")
elif len(playerone.personaldeck) == 0:
    print("YOU WON! THE WINNER IS: {}\n".format(playertwo.name))
print("THANK YOU FOR PLAYING! SEE YOU NEXT TIME")
