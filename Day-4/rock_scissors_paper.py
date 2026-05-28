# Rock, Paper, Scissors Game

import random

computer_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_choices)
# print(f"Computer chose: {computer_choice}")


user_choice = input("Enter your choice (rock=0, paper=1, scissors=2): ").lower()

if(user_choice=="0"):
    user_choice = "rock"
elif(user_choice=="1"):
    user_choice = "paper"
elif(user_choice=="2"):
    user_choice = "scissors"
else:
    print("Invalid choice! Please choose 0, 1, or 2.")
    exit()

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if(user_choice == "rock" and computer_choice == "scissors"):
    print("You win! Rock beats Scissors.")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("You win! Scissors beats Paper.")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("You win! Paper beats Rock.")
elif(user_choice == computer_choice):
    print("It's a tie!")
else:
    print("Computer wins!")