#Write either ACE check or Hand Check not both!
#Hand check has been split out
#
#Create Dealer AI

import random
import sys
4
class blackjack:
  def __init__(self):
    pass
  
  def play(self):
    self.deck = self.createDeck()
    self.yourHand()
  
  def yourHand(self):
    self.answer = input("Would you like to play? Yes/No :")

    if self.answer.lower() != "yes":
      print("Screw you anyway....")
      return

    print("Dealing...")
    self.hand = list()
    self.a = random.choice(self.cards)
    self.b = random.choice(self.cards)
    self.hand.append("ACE!")
    self.hand.append(9)
    self.pontoon = list()
    self.pontoon = ["ACE!", 10]
    if "ACE!" in self.hand:
      if 10 in self.hand:
        print("woohoo")
        print(self.hand)
        self.house()
      else:
        self.playYourHand()
    else:
      self.playYourHand()


  def aceCheck(self):
      if "ACE!" in self.hand:
          print(self.hand)
          self.Ace_a = input("Would you like Ace to be 1 or 11?:")
          if self.Ace_a == 1 or 11:
            self.tempHand = []
            for each in self.hand:
              if each == "ACE!":
                break
              else:
                self.tempHand.append(each)  
            self.Ace_a =  int(self.Ace_a) + int(sum(self.tempHand))
            if self.Ace_a > 21:
              print("Buster")
              sys.exit()
            else:
              print(self.hand)
                  
          else:
            print("Are ya deaf? 1 or 11?:")
  
  def fiveCardCheck(self):
    if len(self.hand) >= 5:
      print(self.hand)
      print("you win!")
      sys.exit()
  
  def handcheck(self):
      if sum(self.hand) == 21:
        print("You win!!")
        print("Game Over")
        self.house()
        break
      if sum(self.hand) >21:
        print("Bust.")
        print("Game Over")
        self.house()
        break

  def playYourHand(self):
    self.aceCheck()
    self.fiveCardCheck()
    while True:
      self.aceCheck()
      self.fiveCardCheck()
      print(self.hand)
      self.playhand = self.hand
      i = 0
      for each in self.playhand:
        if each == "ACE!":
          self.playhand[i] = input("Would you like 1 or 11")
        else:
          continue   

      while True:
        self.choice = input("Stick or Twist:")
        if self.choice.lower() == "stick":
          print("Coward")
          print(self.hand)
          self.house()
          return
        if self.choice.lower() =="twist":
          self.dealt = random.choice(self.cards)
          self.hand.append(self.dealt)
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


  def house(self):
    print("test")


test = blackjack().play()

print(test)
    




    
    


