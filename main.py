#Rock, Paper, Scissors#
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

print("Welcome to Game")

# Take input from user
choice = input("What is your choice? rock,paper or scissors\n").lower()
if choice == "rock":
    print(rock)
elif choice == "paper":
    print(paper)
else:
    print(scissors)


my_list = ["rock", "paper", "scissors"]
computer_choice = (random.choice(my_list)) # Creat a random choice for computer
if computer_choice == "rock":
    print("rock", rock)
elif computer_choice == "paper":
    print("paper", paper)
else:
    print('scissors',scissors)

# code for result
if choice == "rock" and computer_choice == "scissors":
    print("Congratulation, you are winner!")
elif choice=="scissors" and computer_choice == "paper":
    print("Congratulations, you are winner!")
elif choice=="paper" and computer_choice == "rock":
    print("Congratulations, you are winner!")
else:
    print("You lose game")


