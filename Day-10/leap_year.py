def leap_year1(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def leap_year2(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leap_year1(int(input("Enter a year: "))))  
print(leap_year2(int(input("Enter a year: "))))  
