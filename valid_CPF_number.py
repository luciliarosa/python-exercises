#Simple program to check if a CPF number is valid

def valid_CPF_number (number):
    if not number.isdigit():
        return "Error! The CPF number must contain only numbers"
    if len(number) != 11:
        return "Error! The CPF number must contain only 11 digits"
    return "CPF Valid!"

CPF_number = input("Enter your CPF Number: ")
print(valid_CPF_number(CPF_number))
