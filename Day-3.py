# ============================================================
# IF / ELSE - Voting Eligibility
# ============================================================
age = int(input("What is your age?\n"))

if age >= 18:
    print("You can vote")
else:
    print("You can not vote")


# ============================================================
# MODULO OPERATOR - Returns remainder of division
# 7 % 2 = 1 (7 divided by 2 leaves remainder 1)
# ============================================================
print(7 % 2)


# ============================================================
# ODD OR EVEN - If remainder is 0 when divided by 2 → even
# ============================================================
number = int(input("Input the number\n"))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# ============================================================
# NESTED IF / ELSE - Voting + Citizen Category
# Outer if checks voting age, inner if checks citizen type
# ============================================================
age = int(input("What is your age?\n"))

if age >= 18:
    print("You can vote")
    if age <= 50:
        print("and you are senior citizen")
    elif age >= 70:
        print("and you are super senior citizen")
    else:
        print("and you are not senior citizen")
else:
    print("You can not vote")


# ============================================================
# BMI CALCULATOR
# Formula: weight (kg) / height (m) squared
# < 18.5 → underweight | 18.5–25 → normal | >= 25 → overweight
# ============================================================
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")


# ============================================================
# RESTAURANT ORDER - Age based food + price calculator
# Base price = 10, extra cost added based on age group
# ============================================================
age = int(input("Food: What is your age?\n"))
price = 10   # base price
extra = 0    # extra charge based on age
total = 0

if age <= 50:
    if age < 10:
        print("Take ice cream")
        extra = 1
    elif age >= 10 and age < 20:
        print("Take biryani")
        extra = 2
    elif age >= 20 and age < 30:
        print("Take baby corn")
        extra = 3
    else:
        print("Take nothing")
    total = price + extra   # final bill = base + extra
    print(total)
else:
    print("Your age is more than 50")


# ============================================================
# PIZZA DELIVERY BILL CALCULATOR
# Base price depends on size, toppings add extra cost
# S=15 | M=20 | L=25 | Pepperoni S=+2, M/L=+3 | Cheese=+1
# ============================================================
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0

if size == "S":
    total = 15
    if pepperoni == "Y":
        total += 2          # small pepperoni costs $2
elif size == "M":
    total = 20
    if pepperoni == "Y":
        total += 3          # medium pepperoni costs $3
elif size == "L":
    total = 25
    if pepperoni == "Y":
        total += 3          # large pepperoni costs $3

if extra_cheese == "Y":
    total += 1              # extra cheese is $1 for any size

print(f"Your final bill is: ${total}.")


# ============================================================
# TREASURE ISLAND GAME - Choose your path to find treasure
# Wrong choices = Game Over | Only correct path = You Win
# ============================================================
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("Left or Right\n").lower()   # .lower() accepts any case input

if left_right == "left":
    swim_wait = input("Swim or Wait\n").lower()
    if swim_wait == "wait":
        blue_yellow_red = input("Which door?\n").lower()
        if blue_yellow_red == "blue":
            print("Eaten by beasts. Game Over.")
        elif blue_yellow_red == "red":
            print("Burned by fire. Game Over.")
        elif blue_yellow_red == "yellow":
            print("You Win!")                   # only winning path
        else:
            print("Game Over.")                 # any other input loses
    else:
        print("Attacked by trout. Game Over.")  # swimming = danger
else:
    print("Fall into a hole. Game Over.")       # going right = instant loss