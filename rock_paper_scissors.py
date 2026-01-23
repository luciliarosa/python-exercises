
import random

def rock_paper_scissors():
    choice = ["rock", "paper", "scissors"] 
    computer_chose = random.choice(choice) 
    user_chose = input("Choise: rock, paper ou scissors? ").lower() 

    if user_chose not in choice: 
        print("Invalid choise!") 
        return 

    print(f"Computador escolheu: {computer_chose}") 

    if user_chose == computer_chose: 
        print("Draw!") 
    elif ( 
        (user_chose == "rock" and computer_chose == "scissors") or 
        (user_chose == "paper" and computer_chose == "rock") or 
        (user_chose == "scissors" and computer_chose == "paper") 
    ): 
        print("You won!") 
    else: 
        print("You lost!") 

rock_paper_scissors()




    