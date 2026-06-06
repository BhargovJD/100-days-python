from prettytable import PrettyTable

# Create table
table = PrettyTable()

# Add columns
table.add_column("ID", [1, 2, 3])
table.add_column("Name", ["Rahul", "Priya", "Amit"])
table.add_column("Age", [25, 23, 28])


# Print table
print(table)