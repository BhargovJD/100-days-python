import random

number = random.randint(10, 20)
print("Welcome to the Guessing Game!")
print(f"System number : {number}")  # You can comment this out to hide the number

while True:
    guess = int(input("Guess a number between 10 and 20: "))
    
    if guess == number:
        print("Congratulations! You guessed the number.")
        print("The number was:", number)
        break        # exit the loop when guess is correct
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")