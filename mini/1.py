import random


def guess_number(x):
    The_num = random.randint(1,x)
    if(x<=10):
        print("Lol this is to small range you shouldn't take more than 3 attempts 😂")
    elif(x<=100):
        print("This is an ideal range hope you will guess in less than 8 attempts 🙂")
    else:
        print("Ohh..my, The range is big you should try your luck..🥵")
    user_guess = 0
    count = 0
    while(user_guess != The_num):
        if(count==0):
            print(f"Okk, we will start... I hope you are very excited for your first guess 🌠 ")
        else:
            print(f"This is your {count+1} attempt, please tell your number:")
        user_guess = float(input())
        count += 1
        if(user_guess==The_num):
            print(f"congrats you guessed the number correctly 🥳 you took {count} attempts")
            if(count <= 5):
                print("Wow! you guessed it so quickly 🥵")
            elif(count>5 and count <=10):
                print("Heyy...You have to the ability to become a best guesser, Hope you will improve! 😅")
            elif(count > 10 and count <=15):
                print("Note: Not so fast but you can definetly improve...👍")
            else:
                print("But Learn to guess more properly, after all you just have to guess a fucking integer!!")
        elif(user_guess>The_num):
            print("Oops you guessed too big 😒 ")
        else:
            print("Oops 🥲 you guessed too small")



guess_number(1000)


