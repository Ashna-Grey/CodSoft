import random
def get_choice_name(choice):
    return {1: "Rock", 2: "Paper", 3: "Scissors"}.get(choice)
def counter_move(choice):
    return {1: 2, 2: 3, 3: 1}[choice]
while True:
    print("\n--- Rock Paper Scissors ---")
    user_choice_counts = {1: 0, 2: 0, 3: 0}
    for round_num in range(1, 4):
        print(f"\nRound {round_num}:")
        print("1 = Rock")
        print("2 = Paper")
        print("3 = Scissors")
        while True:
            try:
                user_choice = int(input("Enter your choice (1/2/3): "))
                if user_choice not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Enter 1, 2, or 3.")
        user_choice_counts[user_choice] += 1
        if round_num >= 2:
            predicted_user_move = max(user_choice_counts, key=user_choice_counts.get)
            computer_choice = counter_move(predicted_user_move)
        else:
            computer_choice = random.randint(1, 3)
        print(f"You chose: {get_choice_name(user_choice)}")
        print(f"Computer chose: {get_choice_name(computer_choice)}")
        if user_choice == computer_choice:
            print("Result: It's a Draw!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("Result: You Win!")
        else:
            print("Result: Computer Wins!")
    play_again = input("\n3 rounds completed. Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
