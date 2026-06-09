# Example 1
class Student:
    name = "John Doe"

s1 = Student()
print(Student.name)  # Output: John Doe
print(s1.name)      # Output: John Doe
print("......................")

# Example 2
class Car:
    color = "blue"
    brand = "Toyota"

car1 = Car()
print(car1.color)  # Output: blue
print(car1.brand)  # Output: Toyota
print("......................")

# Example 3: parameterized constructor
class Student:
    def __init__(self, name):
        print("Constructor called")
        self.name = name

s1 = Student("Alice")
print(s1.name)  # Output: Alice
s2 = Student("Bob")
print(s2.name)  # Output: Bob
print("......................")

# Example 4: default constructor
class Student:

    # Default constructor
    def __init__(self):
        print("Default constructor called")

    def __init__(self):
        print("Default constructor called2")

s1 = Student()  # Output: Default constructor called2
print("......................")
    
# Example 4: default constructor with parameterized constructor
class Student:

    # Default constructor
    def __init__(self):
        print("Default constructor called")

    def __init__(self,name):
        print("Parameterized constructor called")
        self.name = name

s1 = Student("Alice")  # Output: Parameterized constructor called
print(s1.name)  # Output: Alice
print("......................")

# Example 5:
class Student:
    college = "ABC College"
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 20)
print(s1.name)     # Output: Alice
print(s1.age)      # Output: 20
print(s1.college)  # Output: ABC College
# college is a class variable, it is shared among all instances of the class. 
# It can be accessed using the class name or the instance name.
print(Student.college)  # Output: ABC College
print("......................")

# Example 6: Class with method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 20)
s1.display()  # Output: Name: Alice, Age: 20
print("......................")

# Example 7: Static method
# A static method is used when a function belongs to a class 
# but does not need access to the object (self) or the class.
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))
    
