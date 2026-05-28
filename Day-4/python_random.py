import random
import my_module

# random integer between 1 and 10
random_number = random.randint(1, 10)
print(random_number)


# using custom module
print(f"My favorite number is {my_module.my_fav_number}")


# random float between 0 and 1
# 0.0≤x<1.0
random_float = random.random()
print(random_float)

# Head or Tail
coin = random.randint(0,1)
if(coin == 0):
    print("Heads")
else:
    print("Tails")