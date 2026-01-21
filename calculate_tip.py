#Simple program to calculate the bill and tip

def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

bill_amount = float(input('Enter the amount of the bill: '))
tip_percentage = float(input('Enter the percentage of the tip: '))

tip_amount = calculate_tip(bill_amount, tip_percentage)
total_amount = bill_amount + tip_amount

print(f'Tip amount: ${tip_amount:.2f}')
print(f'Total amount: ${total_amount:.2f}')