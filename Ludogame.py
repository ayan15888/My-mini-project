import random as r
def dice():
    print("Welcome to ludo")
    lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 6]
    first_outcome = r.choice(lst)
    print(first_outcome)
    if (first_outcome != 6):
        print(f"You have to move {first_outcome}")
    elif (first_outcome == 6):
        second_turn = r.choice(lst)
        print(second_turn)
        while (second_turn != 6):
            print(first_outcome+second_turn)
            print(f"You have to move {first_outcome+second_turn}")
            break
        if (second_turn == 6):
            third_chance = r.choice(lst)
            print(third_chance)
            if (third_chance != 6):
                total = first_outcome+second_turn+third_chance
                print(f"You have to move: {total}")
            else:
                print("You are not allowed to move")
dice()
