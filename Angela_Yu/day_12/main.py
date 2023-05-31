import random

r=random.randint(1,100)
print(r)



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty=input("choose a difficulty. Type 'easy' or 'hard':")
if difficulty=='easy':
  attempts=10
if difficulty=='hard':
  attempts=5

def check(guess,attempts):
  if guess==r:
    print("You Guessed it right")
  if guess>r:
    print("Too High")
    print("Guess Again")
    attempts=attempts-1
    print(f"You have {attempts} attempts remaining\n")
  if guess<r:
    print("Too Low")
    print("Guess Again")
    attempts=attempts-1
    print(f"You have {attempts} attempts remaining\n")
  
  
while attempts!= 0:
  guess=int(input(("Enter Your Guess")))
  check(guess,attempts)
  
