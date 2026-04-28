import random

choices = ["rock", "paper", "scissors"]

def check_winner(p1, p2, move1, move2):
    print(f"\n{p1} chose: {move1}")
    print(f"{p2} chose: {move2}")

    if move1 == move2:
        print("Round Draw!")

    elif (move1 == "rock" and move2 == "scissors") or \
         (move1 == "paper" and move2 == "rock") or \
         (move1 == "scissors" and move2 == "paper"):
        print(f"{p1} Wins This Round!")

    else:
        print(f"{p2} Wins This Round!")


while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        p1 = input("Enter Player 1 Name: ")
        p2 = input("Enter Player 2 Name: ")

        rounds = int(input("Enter number of rounds (1 to 5): "))

        if rounds < 1 or rounds > 5:
            print("Please enter rounds between 1 and 5 only.")
            continue

        for i in range(1, rounds + 1):
            print(f"\n--- Round {i} ---")
            move1 = input(f"{p1}, enter rock/paper/scissors: ").lower()
            move2 = input(f"{p2}, enter rock/paper/scissors: ").lower()

            if move1 not in choices or move2 not in choices:
                print("Invalid move! Try again.")
                continue

            check_winner(p1, p2, move1, move2)

    elif choice == "2":
        p1 = input("Enter Player Name: ")
        p2 = "Computer"

        rounds = int(input("Enter number of rounds (1 to 5): "))

        if rounds < 1 or rounds > 5:
            print("Please enter rounds between 1 and 5 only.")
            continue

        for i in range(1, rounds + 1):
            print(f"\n--- Round {i} ---")
            move1 = input(f"{p1}, enter rock/paper/scissors: ").lower()
            move2 = random.choice(choices)

            if move1 not in choices:
                print("Invalid move! Try again.")
                continue

            check_winner(p1, p2, move1, move2)

    elif choice == "3":
        print("Thank You! Game Exited.")
        break

    else:
        print("Invalid choice!")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again == "no":
        print("Thank You! Game Exited.")
        break