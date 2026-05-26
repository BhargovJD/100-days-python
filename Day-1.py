# ===== PRINT STATEMENTS =====

# Prints 'hello world' on one line
print("hello world")

# \n is a newline character — prints 'hello' and 'world' on separate lines
print("hello\nworld")

# Concatenates (joins) three strings with + operator to print 'Hello world'
print("Hello" + " " + "world")


# ===== USER INPUT =====

# input() pauses the program and waits for the user to type something
# Whatever the user types gets stored in the 'name' variable
name = input("What is your name?")

# Joins the name with surrounding text using + and prints it
print("Your name is: " + name + "!")

# input() can be used directly inside print() without storing in a variable
print("Your city name is : " + input("What is your city name?") + "!")


# ===== VARIABLES =====

# A variable stores a value — here 'name' stores the string "Bhargov"
name = "Bhargov"
print(name)  # prints: Bhargov


# ===== STRING LENGTH =====

# len() returns the number of characters in a string
# "Bhargov" has 7 characters
print(len(name))  # prints: 7


# ===== SWAP TWO VARIABLES =====

# Initial values
glass1 = "milk"
glass2 = "juice"

# Step 1: Save glass2's value in a temporary variable so we don't lose it
temp = glass2       # temp   = "juice"

# Step 2: Copy glass1's value into glass2
glass2 = glass1     # glass2 = "milk"

# Step 3: Assign the saved temp value to glass1
glass1 = temp       # glass1 = "juice"

print(glass2)       # prints: milk


# ===== BAND NAME GENERATOR =====

print("Welcome to the Band Name Generator.")

# Ask the user for their city and store the answer
city = input("What city did you grow up?\n")

# Ask the user for their pet name and store the answer
pet_name = input("What is your favorite pet?\n")

# Combine city + pet name to create a fun band name
print("Your brand name is: " + city + pet_name)