import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def main():

    while True:
        # Display welcome message
        print("Welcome to rock, paper, scissors")


        # Player choice
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Computer choice
        computer = computer_choice()

        # Output 
        print(f"Computer chose: {computer}")

        if player_choice == computer:
            print("It's a tie")
        elif (player_choice == "scissors" and computer == "rock") or \
            (player_choice == "rock" and computer == "paper") or \
            (player_choice == "paper" and computer == "scissors"):
            print("Computer wins")
        else:
            print("You win")

        # Ask to repeat game
        repeat_game = input("Would you like to play again (yes/no)? ").lower()

        if repeat_game == "no":
            print("Thanks for playing!")
            break

        elif repeat_game == "yes":
            continue

        else: 
            print("Invalid reponse")
            break

if __name__ == "__main__":
    main()




