import random
def number_game():
    number_guess = random.randint(1, 100)
    print("hello! welcome the game")
    print(" geuss number")
    attempts = 0
    while True:
        user_geuss = input("enter your geuss:")
        if not user_geuss.isdigit():
            print("enter your geuss:")
            continue
        user_geuss = int(user_geuss)
        attempts += 1
        if user_geuss < number_guess:
            print("your number is too low, please try again")
        elif user_geuss > number_guess:
            print("your number is too high, please try again")
        else:
            print("great! you guessed it right")
            print("your number of attempts:",{attempts})
            break
number_game()