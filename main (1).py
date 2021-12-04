import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_shape= "shape"
#Player input
player_choice= int(input("What do you choose? Type 0 for Rock, 1 for Scissors or 2 for Paper.\n"))
if player_choice == 0: 
  print(rock)
  player_shape = "rock"
  print(f"you chose: {player_shape}")
if player_choice == 1:
  print(scissors)
  player_shape = "scissors"
  print(f"you chose: {player_shape}")
if player_choice == 2:
  print(paper)
  player_shape = "paper"
  print(f"you chose: {player_shape}")
#Computer input
#computer_choice= random.randint(0,2)
shapes= ["rock", "paper","scissors"]
computer_choice= random.choice(shapes)
print(f"Computer chose: {computer_choice} ")
if computer_choice =="rock": 
  print(rock)
if computer_choice =="paper": 
  print(paper)
if computer_choice =="scissors": 
  print(scissors)
#Determing winner/draw:
#if the player chooses a number that doesn't correspond to any shape: 
if player_shape != "rock" and player_shape != "scissors" and player_shape != "paper":
  print(f"Computer chose {computer_choice} and you didn't choose one of the three shapes, you lose!")
#In case of a draw:
elif player_shape == computer_choice: 
  print("it's a draw")
#We treat all the 3 cases where the computer wins, else the player will win 
else:
  if computer_choice=="rock" and player_shape== "scissors":
    print("You lose!")
  elif computer_choice=='scissors' and player_shape=="paper":
    print("You lose!")
  elif computer_choice=='paper' and player_shape=='rock':
    print("You lose!")
  else:
    print("You win!")
