
#Creates Deck of cards
cards = list()
for each in range(2,11):
  cards.append(each)
  cards.append(each)
  cards.append(each)
  cards.append(each)
  if each == 10:
    for each in range(0,12):
      cards.append(10)
    for each in range(0,4):
      cards.append("ACE!")
print(cards)


answer = input("Would you like to play? Yes/No :")

if answer.lower() != "yes":
  print("Screw you anyway....")
  quit()

print("Dealing...")
hand = list()
a = random.choice(cards)
b = random.choice(cards)
if a == "ACE!":
  while True:
    Ace_a = input("Would you like Ace to be 1 or 11?:")
    if Ace_a == 1 or 11:
      hand.append(int(Ace_a))
      cards.remove(a)
      break
    else:
      print("Are ya deaf? 1 or 11?:")
if a != "ACE!":
  hand.append(a)
  cards.remove(a)

while True:
  a = random.choice(cards)
  if a == "ACE!":
    while True:
      Ace_a = input("Would you like Ace to be 1 or 11?:")
      if Ace_a == 1 or 11:
        hand.append(int(Ace_a))
        cards.remove(a)
        break
      else:
        print("Are ya deaf? 1 or 11?:")
  if a != "ACE!":
    hand.append(a)
    cards.remove(a)
  print(hand)
  if sum(hand) == 21:
    print("You win!!")
    print("Game Over")
    break
  if sum(hand) >21:
    print("Bust.")
    print("Game Over")
    break
  while True:
    choice = input("Stick or Twist:")
    if choice.lower() == "stick":
      print("Coward")
      print(hand)
      quit()
    if choice.lower() =="twist":
      break
    else:
      print("Stick or Twist, it's not hard!")