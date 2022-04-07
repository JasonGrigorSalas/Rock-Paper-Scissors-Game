from random import randint
choices = ["sword", "shield", "fist"]
player_lives = 3
computer_lives = 3
total_lives = 3
player_choice = False
def win_or_lose(status):
    print("You ", status, " Would you like to play again?")
    choice = input("Y/N ")
    if choice == "N" or choice == "n":
        print("Hope you play again soon! Farewell! :D \n")
        exit()
    elif choice == "Y" or choice == "y":
        global player_lives
        global computer_lives
        global total_lives
        player_lives = total_lives
        computer_lives = total_lives
    else:
        print(" ._. \n")
        choice = input("Y/N ")

while player_choice is False:
    print("******** Sword Shield Fist ********")
    print("Computer lives: ", computer_lives, "/", total_lives)
    print("Player lives: ", player_lives, "/", total_lives)
    print("***********************************\n")
    print("Choose your weapon! Or, if ye be a coward, type quit to exit. \n")
    player_choice = input("Choose sword, shield, or fist: ")
    if player_choice == "quit":
        print("Hope you play again soon! Farewell! :D \n")
        exit()

    print("User chose: " + player_choice)
    computer_choice = choices[randint(0, 2)]
    print("Computer chose: " + computer_choice)
    if computer_choice == player_choice:
        print("Tie. :/ \n")

    elif computer_choice == "sword":
        if player_choice == "fist":
            print("You lose! :( \n")
            # player_lives = player_lives - 1
            player_lives -= 1
        else:
            print("You win! :) \n")
            computer_lives -= 1

    elif computer_choice == "shield":
        if player_choice == "sword":
            print("You lose! :( \n")
            player_lives -= 1
        else:
            print("You win! :) \n")
            computer_lives -= 1

    elif computer_choice == "fist":
        if player_choice == "shield":
            print("You lose! :( \n")
            player_lives -= 1
        else:
            print("You win! :) \n")
            computer_lives -= 1

    if player_lives == 0:
        win_or_lose("lose! :( \n")

    if computer_lives == 0:
        win_or_lose("win! :) \n")

    print("Player lives: ", player_lives)
    print("Computer lives: ", computer_lives)
    player_choice = False
