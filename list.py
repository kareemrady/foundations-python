import re
import os
import platform
import time


def match_letters(input):
    # return false if empty string is entered
    # or if numbers are entered as string rather than actual words
    regex_string = re.compile('[a-zA-Z]+')
    return regex_string.match(input)


def get_user_input():
    print("Add item or type [q] to save list to file and quit\n")
    user_input = raw_input("What item would you like to add to your list?\n")
    return user_input


def add_to_list(item, shopping_list):
    shopping_list.append(item)


def show_list(shopping_list):
    print("Items in your list: \n------------------------------------")
    for item in shopping_list:
        print('- ' + item)


def save_to_file(shopping_list):
    with open('lists.txt', 'w') as f:
        f.write("Your Shopping List \n-------------------\n")
        for item in shopping_list:
            f.write('- ' + item + '\n')


def detect_clear_string():
    operating_sys = platform.system()
    if operating_sys == 'Linux':
        return 'clear'
    else:
        return 'cls'


def new_shopping_list():
    clear_screen_string = detect_clear_string()
    shopping_list = []
    while 1:
        os.system(clear_screen_string)
        user_input = get_user_input()
        user_input_cap = user_input.upper()
        if user_input_cap == "Q":
            print("Saving your list to file........................")
            time.sleep(2)
            save_to_file(shopping_list)
            break
        elif user_input and match_letters(user_input):
            print("Adding item to list........................")
            time.sleep(2)
            add_to_list(user_input, shopping_list)
        else:
            print("Invalid Input")
    show_list(shopping_list)


new_shopping_list()
