import random
import art
from game_data import data
from replit import clear

def check(a,b,guess):
  if a["follower_count"] > b["follower_count"]:
    return guess == "a"
  else:
    return guess == "b"
def play():
  should_continue=True

  b=random.choice(data)
  while should_continue is True:
    
    print(art.logo)
    score=0
    a=b
    b=random.choice(data)
    while a==b:
      b=random.choice(data)
    
    
        
    
    a_name=a["name"]
    a_desc=a["description"]
    a_coun=a["country"]
    
    
    print(f"{a_name},a {a_desc}, from {a_coun}")
    
    print(art.vs)
    
    b_name=b["name"]
    b_desc=b["description"]
    b_coun=b["country"]
    print(f"{b_name},a {b_desc}, from {b_coun}")
    
    users_input=(input("Enter Your Prediction"))
    is_correct = check(a,b,users_input)

    clear()
    
    if is_correct:
      score+=1
      print(f"You'r Right!, And Your score is {score}")
    else:
      print(f"You'r Wrong!, Your Score is {score}")
      should_continue=False

play()
aa=input("Do you want to continue, type 'y' or 'no'")
if aa=='y':
  play()
