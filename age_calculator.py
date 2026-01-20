# Simple program to calculate a person's age based on birth year and current year.

def calculator(birth_year, current_year):
    return current_year - birth_year 

birth = int(input('What year were you born?: ')) 
current = int(input('What is the current year?: '))

age = calculator (birth, current)
print(f'Your age is: {age} years')