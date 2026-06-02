# Black jack game
import random

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start == "y":

    pick_again = "y"

    while pick_again == "y":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        print(f"\nYour cards: {num1}, {num2}")
        your_result = num1 + num2
        print(f"Your score: {your_result}")

        num3 = random.randint(0, 9)
        num4 = random.randint(0, 9)

        print(f"Computer's cards: {num3}, {num4}")
        computer_result = num3 + num4
        print(f"Computer's score: {computer_result}")

        if your_result > computer_result:
            print("You win!")
        elif your_result < computer_result:
            print("Computer wins!")
        else:
            print("Draw!")

        pick_again = input("\nDo you want to play again? Type 'y' or 'n': ")

else:
    print("END")