import random
options=("rock", "paper", "scissors")
compouter_choice = random.choice(options)
user_choice = input("Enter your choice (rock, paper, scissors): ")
print("Computer choice:", compouter_choice)
if user_choice == compouter_choice:
    print("It's a tie!")
elif user_choice == "rock"and compouter_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and compouter_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and compouter_choice == "paper":
    print("You win!")
else:
    print("You lose!")    