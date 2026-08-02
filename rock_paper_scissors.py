import random

convt = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def win(x, y):
    if x == y:
        return "Draw"

    elif x == 1:
        if y == 2:
            return "You Win"
        elif y == 3:
            return "You Lost"

    elif x == 2:
        if y == 1:
            return "You Lost"
        elif y == 3:
            return "You Win"

    elif x == 3:
        if y == 2:
            return "You Lost"
        elif y == 1:
            return "You Win"


while True:
    comp = random.randint(1, 3)

    user = input("Enter your choice (rock/paper/scissors): ").lower()

    if user not in convt:
        print("Invalid choice. Try again.\n")
        continue

    inp = convt[user]

    for key, value in convt.items():
        if comp == value:
            print("Computer choice:", key)
            break

    print(win(comp, inp))

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        exit()
