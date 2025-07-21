import random
def get_choice(choice):
    return {1: "rock", 2: "paper", 3: "scissors"}.get(choice)
def rules(comp_choice, user_choice):
    if (comp_choice == "rock" and user_choice == "scissors") or \
       (comp_choice == "paper" and user_choice == "rock") or \
       (comp_choice == "scissors" and user_choice == "paper"):
        return [1, 0]
    elif comp_choice == user_choice:
        return [0, 0]
    else:
        return [0, 1]
def user_choice():
    print("Enter: \n1->Rock\n2->Paper\n3->Scissors\n")
    try:
        choice = int(input("Enter number: "))
        user_choice = get_choice(choice)
        if not user_choice:
            print("Invalid input. Try again.\n")
            return None
        return user_choice
    except ValueError:
        print("Please enter a valid number (1, 2, or 3).\n")
        return None
def round_result(u_ch, c_ch, result):
    if result == [1, 0]:
        print(f"\nYour choice: {u_ch}\nComputer choice: {c_ch}\nComputer wins!\n")
    elif result == [0, 1]:
        print(f"\nYour choice: {u_ch}\nComputer choice: {c_ch}\nYou win!\n")
    else:
        print(f"\nYour choice: {u_ch}\nComputer choice: {c_ch}\nTie!\n")
def final_result(user_score, comp_score):
    if user_score > comp_score:
        print(f"\nYour score: {user_score}\nComputer score: {comp_score}\nYou win!\n")
    elif user_score == comp_score:
        print(f"\nYour score: {user_score}\nComputer score: {comp_score}\nTie!\n")
    else:
        print(f"\nYour score: {user_score}\nComputer score: {comp_score}\nComputer wins!\n")
while True:
    user_score, comp_score = 0, 0
    for i in range(3):
        u_ch=None
        while not u_ch:
            u_ch=user_choice()
        c_ch=get_choice(random.randint(1,3))
        result=rules(c_ch,u_ch)
        user_score+=result[1]
        comp_score+=result[0]
        round_result(u_ch,c_ch,result)
    final_result(user_score,comp_score)
    yn=input("Do you want to continue? (Y/N): ")
    if yn.lower()=="y":
        continue
    elif yn.lower()=="n":
        break
    else:
        print("Incorrect input")
        break
