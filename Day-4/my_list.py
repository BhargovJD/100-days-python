# list:
    # Ordered
    # Mutable
    # Allows Duplicate Values
    # Can Store Different Data Types
    # Dynamic Size



my_list = ["Alice", "Bob", "Charlie"]
print(my_list[0])  # Output: 'Alice'
print(my_list[1])  # Output: 'Bob'
print(my_list[2])  # Output: 'Charlie'

print(my_list[-1]) # Output: 'Charlie'
print(my_list[-2]) # Output: 'Bob'
print(my_list[-3]) # Output: 'Alice'   
print(my_list)  # Output: ['Alice', 'Bob', 'Charlie'] 

my_list[0] = "David"
print(my_list)  # Output: ['David', 'Bob', 'Charlie']


my_list.append("Eve") # at the end of the list
print(my_list)  # Output: ['David', 'Bob', 'Charlie', 'Eve']

# who gonna pay the bill?
import random
who_pays = random.randint(0, len(my_list) - 1)
print(f"{my_list[who_pays]} is going to pay the bill!")

# or
who_pays = random.choice(my_list)
print(f"{who_pays} is going to pay the bill!")


# Nested List
list_1 = [1, 2, 3 ]
list_2 = [4, 5, 6]
nested_list = [list_1, list_2]  
print(nested_list)  # Output: [[1, 2, 3], [4, 5, 6]]
print(nested_list[0])  # Output: [1, 2, 3]