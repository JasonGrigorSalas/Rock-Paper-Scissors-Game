from random import randint
choices = ["rock", "paper", "scissors"]
# player_choice = choices[0]
# print("Index 0 in the choice array is " + player_choice + ", which is Rock.")
player_choice = input("Choose rock, paper, or scissors: ")
print("User chose: " + player_choice)
computer_choice = choices[randint(0, 2)]
print("Computer chose: " + computer_choice)
if computer_choice == player_choice:
    print("Tie :/")

elif computer_choice == "rock":
    if player_choice == "scissors":
        print("You lose! :(")
    else:
        print("You win! :)")

elif computer_choice == "paper":
    if player_choice == "scissors":
        print("You win! :)")
    else:
        print("You lose! :(")

elif computer_choice == "scissors":
    if player_choice == "paper":
        print("You lose! :(")
    else:
        print("You win! :)")
