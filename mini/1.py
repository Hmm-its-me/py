import random


def guess_number(x):
    The_num = random.randint(1,x)
    user_guess = 0
    count = 0
    while(user_guess != The_num):
        user_guess = int(input())
        count += 1
        if(user_guess==The_num):
            print(f"congrats you guessed the number correctly in {count} attempts")
        elif(user_guess>The_num):
            print("oops you guessed too big 😒")
        else:
            print("oops 🥲 you guessed too small")


