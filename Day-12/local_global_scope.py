# Local Scope
# A variable defined inside a function is local — only accessible within that function.
def greet():
    message = "Hello!"   # local variable
    print(message)       # works

greet()
# print(message)           # NameError: name 'message' is not defined


# Global Scope
# A variable defined at the top level of a script is global — accessible anywhere in the file.

name = "Alice"   # global variable
def greet():
    print(name)  # ✅ can read it

greet()          # prints: Alice
print(name)      # ✅ also works here


# Reading vs. Modifying a Global
# You can read a global inside a function freely, 
# but modifying it requires the global keyword — otherwise Python creates a new local variable instead.

count = 0

def increment():
    global count     # declare intent to modify
    count += 3

increment()
print(count)         # 3