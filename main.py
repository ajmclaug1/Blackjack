#Create dealer AI, need to create Ace logic
#Have it test what would happen if all of the Aces are 1
#Then compare that to the player, then convert one to 11
#then convert the first ace to 11 and test that value is higher than the player but lower than 21
#How to process pontoon



import random
import sys

class blackjack:
  def __init__(self):
    self.HHand = list()
    self.hand = list()
    
  
  def play(self):
    self.deck = self.createDeck()
    self.yourHand()
  
  def yourHand(self):
    self.answer = "yes"#input("Would you like to play? Yes/No :")
    if self.answer.lower() != "yes":
      print("Screw you anyway....")
      return
    print("Dealing...")
    self.a = random.choice(self.cards)
    self.cards.remove(self.a)
    self.b = random.choice(self.cards)
    self.cards.remove(self.b)
    self.hand.append(self.a)
    self.hand.append(self.b)
    self.pontoon = list()
    self.pontoon = ["ACE!", 10]
    if "ACE!" in self.hand:
      if 10 in self.hand:
        print("Woohoo - Pontoon!")
        print(self.hand)
        self.hand = "Pontoon!"
        self.house()
      else:
        self.playYourHand()
    else:
      self.playYourHand()


  def aceCheck(self, player):
    self.player = player
    if "ACE!" in self.hand:
      i = 0 
      for each in self.hand:
        if each == "ACE!":
            self.Ace = input("Would you like Ace to be 1 or 11?:")
            if self.Ace == 1 or 11:
              self.hand[i] = int(self.Ace)
            else:
              print("Are ya deaf? 1 or 11?:")
        i += 1
      print(self.hand)
      if sum(self.hand) > 21:
        print("Buster")
        sys.exit()
    else:
      self.handcheck(self.hand, self.player)
      print(self.hand)


  def fiveCardCheck(self):
    if len(self.hand) >= 5:
      print("This will be tough to beat!")
      self.hand = 50
      self.house()
    if len(self.HHand) >= 5:
      print("This will be tough to beat!")
      self.HHand = 50
      
  
  def handcheck(self,check,player):
    self.check = check
    self.player = player
    i = 0 
    self.temphand = self.check[:]
    for each in self.temphand:
      if each == "ACE!":
          self.temphand[i] = 1
    if sum(self.temphand) >21:
      print("%s Busts" % (self.player))
      print("Game Over")
      print(self.temphand)
      sys.exit()

  def playYourHand(self):
    while True:
      print(self.hand)
      while True:
        self.fiveCardCheck()
        self.decision = input("Stick or Twist:")
        if self.decision.lower() == "stick":
          self.aceCheck("You")
          print("Good luck!")
          self.house()
          return
        if self.decision.lower() =="twist":
          self.dealt = random.choice(self.cards)
          self.hand.append(self.dealt)
          self.cards.remove(self.dealt)
          self.handcheck(self.hand,"player")
          break
        else:
          print("Stick or Twist, it's not hard!")

      
  def createDeck(self):
    #Creates Deck of cards
    self.cards = list()
    for each in range(2,11):
      self.cards.append(each)
      self.cards.append(each)
      self.cards.append(each)
      self.cards.append(each)
      if each == 10:
        for each in range(0,12):
          self.cards.append(10)
        for each in range(0,4):
          self.cards.append("ACE!")
    return self.cards

#AI
  def house(self):
    if self.hand == "Pontoon!":
      print("It's in beta!")
      sys.exit()
    if self.hand == 50:
      print("five cards to win!")
      sys.exit()
    else:
      self.houseplays()
      sys.exit()

  def houseplays(self):
    self.Househand()
    self.HouseAI()


  def Househand(self):
    
    self.a = random.choice(self.cards)
    self.cards.remove(self.a)
    self.b = random.choice(self.cards)
    self.cards.remove(self.b)
    self.HHand.append(self.a)
    self.HHand.append(self.b)
    print("House deals")
    print(self.HHand)

  def HouseAI(self):
    while True:
      if self.HHand == 50:
        print("House wins with a 5 card!")
        sys.exit()

      if "ACE!" in self.HHand:
        print("no Idea")
        return

      else:
        if sum(self.HHand) >= sum(self.hand):
          print("House wins")
          print(self.HHand)
          print(sum(self.HHand))
          return
        else:
          self.dealt = random.choice(self.cards)
          self.HHand.append(self.dealt)
          self.cards.remove(self.dealt)
          self.handcheck(self.HHand,"House")
          self.fiveCardCheck()
          print("House takes a card...")
          print(self.HHand)
  
  def AceLogic(self):
    pass

    


test = blackjack().play()


    




    
    


