# Word Guessing Game

secret_word = "apple"
max_tries = 8
tries = 0

display_word = ["_"] * len(secret_word)
guessed_letters = []

print("Guess the word!")
print(" ".join(display_word))

while tries < max_tries:

    print(f"\nTries Left: {max_tries - tries}")

    letter = input("Enter a letter: ").lower()

    # Validate input
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(letter)

    # Check if letter exists in word
    if letter in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                display_word[i] = letter

        print("✅ Correct!")

    else:
        tries += 1
        print("❌ Wrong!")

    print("Word:", " ".join(display_word))

    # Check if word is completed
    if "_" not in display_word:
        print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
        break

else:
    print(f"\n💀 Game Over! You used all {max_tries} tries.")
    print(f"The word was: {secret_word}")