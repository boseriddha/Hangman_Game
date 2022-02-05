"""
This is a simple hangman game, where you have 6 lives and have to guess the word.
"""

import random
from words import word
import string

def get_valid_words():
    word_item = random.choice(word)
    while '-' in word_item or ' ' in word_item:
        word_item = random.choice(word)

    return word_item

def hangman():
    # getting a word
    new_word = get_valid_words().upper()
    # letters of the word
    word_letters = set(new_word)
    # all the english letters
    alphabet = set(string.ascii_uppercase)
    # what the user has guessed
    used_letters = set()
    # lives
    lives = 6


    while len(word_letters) > 0 and lives > 0:
        # letters user has already used
        print('You have ' + str(lives) + ' lives, and have already used: ' + ' '.join(used_letters))

        # what the current word is (for eg W_RD)
        # print(new_word)
        word_list = [letter if letter in used_letters else '_' for letter in new_word]
        print("Current Word: " + ''.join(word_list))

        # getting user input
        user_letter = input("Enter an alphabet: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("You just lost a live!")
        elif user_letter in used_letters:
            print("You have already guessed it! Try Again!")
        else:
            print("Invalid Character")

    if len(word_letters) == 0:
        print("You guessed it right! The word was " + new_word)
    elif not lives:
        print("You lost! the word was: " + new_word)

# driver code
if __name__ == "__main__":
    hangman()