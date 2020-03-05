#just colors
import random
import replit
deck = ["red", "blue", "green","yellow","Orange"]


player1 = {
  "Name": "Mr.T ",
  "Hand": [ ],
  "Numbers": [ ]
}
player2 = {
  "Name": " Mr.B",
  "Hand": [ ],
  "Numbers": [ ]
}


current_card= random.choice(deck)
current_number = random.randint(0,5)

def deal(player):
  for x in range(6):
    player["Hand"].append (random.choice(deck))
    player["Numbers"].append(random.randint(0,5))


def play_card (player):
  global current_card, current_number
  print("The current card is: ", current_number,current_card)
  print(player["Hand"] )
  print(player["Numbers"])
  choice = input("What card do you want to play? (Type 0 for the 1st card, 5 for the last card) ")
  
  if choice == "0" and (player["Hand"][0] == current_card or player["Numbers"][0] == current_number):
    current_card = player["Hand"][0]
    current_number = player["Numbers"][0]
    del player["Hand"][0]
    del player["Numbers"][0]
  elif choice == "1" and (player["Hand"][1] == current_card or player["Numbers"][1] == current_number):
    current_card = player["Hand"][1]
    current_number = player["Numbers"][1]
    del player["Hand"][1]
    del player["Numbers"][1]
   
  elif choice == "2" and (player["Hand"][2] == current_card or player["Numbers"][2] == current_number):
    current_card = player["Hand"][2]
    current_number = player["Numbers"][2]
    del player["Hand"][2]
    del player["Numbers"][2]
  elif choice == "3" and (player["Hand"][3] == current_card or player["Numbers"][3] == current_number):
    current_card = player["Hand"][3]
    current_number = player["Numbers"][3]
    del player["Hand"][3]
    del player["Numbers"][3]
    
  elif choice == "4" and (player["Hand"][4] == current_card or player["Numbers"][4] == current_number):
    current_card = player["Hand"][4]
    current_number = player["Numbers"][4]
    del player["Hand"][4]
    del player["Numbers"][4]
    
  elif choice == "5" and (player["Hand"][5] == current_card or player["Numbers"][5] == current_number):
    current_card = player["Hand"][5]
    current_number = player["Numbers"][5]
    del player["Hand"][5]
    del player["Numbers"][5]
    
  else:
    if len(player["Hand"]) >= 6:
      print("invalid input, you lost your turn")
    else:
      print("invalid input, draw a card")
      player["Hand"].append(random.choice(deck))
      player["Numbers"].append(random.randint(0,5))

deal(player1)
deal(player2)

def checkWin (player):
  if player["Hand"] == [ ] and player["Numbers"] == [ ]:
    print(player["Name"], " Wins!!!")
    quit()

while True:
  print("player 1 turn!")
  play_card(player1)
  checkWin(player1)
  replit.clear()
  
  print("player 2 turn!")
  play_card(player2)
  checkWin(player2)
  replit.clear()



  