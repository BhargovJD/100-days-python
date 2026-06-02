def my_name(f_name, l_name):
    """This function takes in a first name and a last name, 
    capitalizes the first letter of each name, 
    and returns the full name in the format "FirstName LastName".
    """
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f"{f_name} {l_name}"


print(my_name(f_name="BhArGov", l_name="Das"))

