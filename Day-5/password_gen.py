import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

pick_letters = int(input("How many letters?\n"))
pick_numbers = int(input("How many numbers?\n"))
pick_symbols = int(input("How many symbols?\n"))

added_letters = []
for letter in range(1, pick_letters + 1):
    random_char = random.choice(letters)
    added_letters.append(random_char)

added_numbers = []
for number in range(1, pick_numbers + 1):
    random_num = random.choice(numbers)
    added_numbers.append(random_num)

added_symbols = []
for symbol in range(1, pick_symbols + 1):
    random_symbol = random.choice(symbols)
    added_symbols.append(random_symbol)

# Combine all three lists into one
password_list = added_letters + added_numbers + added_symbols

# Shuffle so characters aren't grouped (letters first, then numbers, then symbols)
random.shuffle(password_list)

print(password_list)

# Join the list into a single string
password = "".join(password_list)
print(f"Your password is: {password}")