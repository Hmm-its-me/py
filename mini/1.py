import random


def guess_number(x):
    The_num = random.randint(1,x)
    user_guess = 0
    count = 0
    while(user_guess != The_num):
        if(count==0):
            print(f"Hello Are you excited for your first guess 🌠 ")
        else:
            print(f"This is your {count+1} attempt, please tell your number:")
        user_guess = float(input())
        count += 1
        if(user_guess==The_num):
            print(f"congrats you guessed the number correctly 🥳 you took {count} attempts")
        elif(user_guess>The_num):
            print("oops you guessed too big 😒 ")
        else:
            print("oops 🥲 you guessed too small")



guess_number(100)
        

