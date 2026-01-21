def somar(a, b):
    return a + b

try: 
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number'))

    resultado = somar (num1, num2)
    print(f'The sum of the numbers is: {resultado}')

except ValueError:
    print('Invalid Number! Please enter only valid numbers.')

