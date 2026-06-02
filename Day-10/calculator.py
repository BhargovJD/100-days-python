def calculator(first_number, second_number, action):

    if action == "+":
        return first_number + second_number

    elif action == "-":
        return first_number - second_number

    elif action == "*":
        return first_number * second_number

    elif action == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            return "Error: Division by zero is not allowed."

    else:
        return "Invalid operation"


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
action = input("Enter the action (+, -, *, /): ")

result = calculator(first_number, second_number, action)

print(f"Result: {result}")