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

            


def computer_guess(y, x):
    print("Please tell your secret number: ")
    The_num = int(input())
    if(x<=10):
        print("Lol this is to small range I will not take more than 3 attempts 😂")
    elif(x<=100):
        print("This is an ideal range, i think i can crack it in less than 8 attempts 🙂")
    else:
        print("Ohh..my, The range is too big i should follow a good strategy..🥵")


    computer_guess = 0
    count = 0
    while(computer_guess != The_num):
        if(count==0):
            print(f"Okk, I will start guessing... I hope you are very excited for my first guess 🌠 ")
        else:
            print(f"This is my {count+1} attempt, I hope I will get this correctly this time...:")
        computer_guess = (y+x)//2
        print(computer_guess)
        count += 1
        if(computer_guess==The_num):
            print(f"Yayy.. I guessed the number correctly 🥳 I took {count} attempts")
            if(count <= 5):
                print("Wow! I guessed it so quickly 😎")
            elif(count>5 and count <=10):
                print("Heyy...I think I have the ability to become a best guesser, Hope I will become the best..😅")
            elif(count > 10 and count <=15):
                print("Not so fast but I can definetly improve...👍")
            else:
                print("I should Learn to guess more properly, after all I just have to guess a fucking integer!!")
        elif(computer_guess>The_num):
            x = computer_guess
            print("Oops did I guessed too big 😒 ")
        else:
            print("Oops 🥲 did I guessed too small")
            y = computer_guess
    

computer_guess(1, 1000)
# guess_number(1000)


