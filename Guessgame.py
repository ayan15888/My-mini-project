import random as r
lst = [1, 2, 3, 4, 5, 6, 8, 9, 10]
dice = r.choice(lst)


def guess_game():
    count = 0
    for i in range(1, 4):
        user_input = int(
            input("Enter any number between 1-10 and try to win in 3 attempt or you will loss \n"))

        if (user_input > 10 or user_input < 0):
            print("Enter valid number")

            guess_game()

        if (user_input == dice):
            print("Well done You guess is correct ")
            break
        elif (user_input != dice):
            print("Try again")

            print(f"You have {3-i} attempt")
            count += 1
    if (count == 3):
        print("YOU LOST")


guess_game()
