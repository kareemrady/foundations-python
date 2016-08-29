import string
import random
import os
import platform
import re
import time

STRING_CHARS = string.ascii_lowercase
GUESSES = 5


def pick_random_letter():
    return random.choice(STRING_CHARS)


def detect_os():
    return platform.system()


def detect_clear_screen_string(os_name):
    if os_name == 'Windows':
        return 'cls'
    else:
        return 'clear'


def clear_screen():
    os_name = detect_os()
    clr_str = detect_clear_screen_string(os_name)
    os.system(clr_str)


def display_welcome_message():
    print("Welcome To Guess the Letter Game")
    print("-----------------------------------\n")


def display_guesses_left(guesses):
    print("You have {0} attempts to guess the right letter\n".format(guesses))


def detect_invalid_letter(input):
    reg_expr = re.compile('^[a-z]')
    return re.match(reg_expr, input)


def get_user_input():
    print("Please Type in a Letter from a-z:")
    user_input = raw_input().lower()
    match_found = detect_invalid_letter(user_input)
    while not match_found:
        print("Invalid Entry, Please Type in a Letter from a-z:")
        user_input = raw_input().lower()
        match_found = detect_invalid_letter(user_input)
    return user_input


def play_game():
    display_welcome_message()
    guesses = GUESSES
    while guesses:
        time.sleep(2)
        clear_screen()
        display_guesses_left(guesses)
        user_choice = get_user_input()
        comp_choice = pick_random_letter()
        if user_choice == comp_choice:
            print("You Guessed it Right !!!!")
            break
        else:
            print("Sorry your guess {} is not correct\n".format(user_choice))
            guesses -= 1
    else:
        print("Sorry You Lost !!!")

play_game()
