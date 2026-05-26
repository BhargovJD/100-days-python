# ===== SUBSCRIPTING (Accessing characters in a string) =====

from math import floor  # importing floor function from math library

# Indexing starts from 0 — 'b' is at position 0
print("bhargov"[0])   # output: b

# Negative index starts from end — 'v' is the last character
print("bhargov"[-1])  # output: v


# ===== DATA TYPES =====

# STRING — text data, written in quotes
# + with strings means CONCATENATION (joining), not addition
print("123" + "456")  # output: 123456 (not 579!)

# INTEGER — whole numbers, + means actual addition
print(3 + 1)          # output: 4

# FLOAT — decimal numbers
print(12.32)          # output: 12.32

# type() — tells you what data type a value is
print(type("Hello"))  # output: <class 'str'>
print(type(123))      # output: <class 'int'>
print(type(True))     # output: <class 'bool'>
print(type(123.23))   # output: <class 'float'>


# ===== TYPE CONVERSION =====

# int() converts string to integer so we can do math on it
# without int(), "123"+"2" would give "1232" (string join)
print(int("123") + int("2"))  # output: 125


# ===== STRING LENGTH =====

# input() takes text from user and stores it in 'name'
name = input("What is your name?")

# len() counts the number of characters in the string
name_length = len(name)

# str() converts integer to string so we can join it with +
print("Total name length is: " + str(name_length))


# ===== PEMDAS / BODMAS (Order of Operations) =====

print(6 + 4 / 2 - (1 * 2))

# Step 1 — Brackets:    (1 * 2) = 2
# Step 2 — Division:     4 / 2  = 2.0
# Step 3 — Addition:    6 + 2.0 = 8.0
# Step 4 — Subtraction: 8.0 - 2 = 6.0
# output: 6.0


# ===== BMI CALCULATOR =====

height = 1.65  # height in metres
weight = 84    # weight in kilograms

# BMI formula = weight / height²
# ** means power/exponent — height ** 2 means height squared
bmi = weight / height ** 2

print(bmi)              # output: 30.89 (full decimal)
print(floor(bmi))       # output: 30    (always rounds DOWN)
print(round(bmi))       # output: 31    (rounds to nearest whole number)
print(round(bmi, 2))    # output: 30.89 (rounds to 2 decimal places)


# ===== F-STRING (modern way to insert variables into strings) =====

# f'' string — put f before the quote, then use {} to insert variables
# cleaner than using + and str() for joining
print(f'hi you are {name}')  # output: hi you are Bhargov


# ===== TIP CALCULATOR =====

# Step 1: Take the total bill
# float() used because bill can have decimals like $10.50
bill = float(input("What was the total bill? $"))

# Step 2: Ask how much tip they want to add
# int() used because tip % is a whole number like 10, 12, 15
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Step 3: Ask how many people to split the bill
# int() used because number of people is always a whole number
people = int(input("How many people to split the bill? "))


# ===== CALCULATION =====

# Convert tip percentage to decimal and multiply by bill
# Example: 10% of $100 = 100 * (10/100) = $10
tip_amount = bill * (tip / 100)

# Add tip to original bill to get total
total = bill + tip_amount

# Divide total equally among all people
split = total / people


# ===== RESULT =====

# round(split, 2) — rounds to 2 decimal places like $22.05
# str() — converts number to string so we can join with +
print("Each person should pay: $" + str(round(split, 2)))