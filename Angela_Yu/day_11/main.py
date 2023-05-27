import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  


def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(comp_score,user_score):
  if(user_score>21 and comp_score>21):
    return "you went over, You lose"
  if user_score==comp_score:
    return "Draw"
  elif comp_score==0:
    return "Lose, opponent have blackjack"
  elif user_score==0:
    return "You, win"
  elif user_score>21:
    return "You went over, You Lose"
  elif comp_score>21:
    return "Opponent went over, You Win"
  elif user_score>comp_score:  
    return "You Win"
  else:
    return "you Lose"

def play():
  user_cards = []
  computer_cards = []
  is_game_over=False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)
    print(f"Your Cards: {user_cards}, current score: {user_score}")
    print(f"computer's Cards: {computer_cards[0]}")
    
    
    if user_score ==0 or comp_score==0 or user_score>21:
      is_game_over=True
    else:
      user_should_deal=input("type 'y' to get another card, type 'no' to pass")
      if user_should_deal=="y":
        user_cards.append(deal_card())
      else:
        is_game_over=True
    
  while comp_score!=0 and comp_score<17:
    computer_cards.append(deal_card())
    comp_score=calculate_score(computer_cards)
  
  print(compare(user_score,comp_score))
  print(f"User's final cards: {user_cards} Score: {user_score}")
  print(f"Computer's final cards: {computer_cards} Score: {comp_score}")

while input("Do you want to play the game again")=='y':
  play()
