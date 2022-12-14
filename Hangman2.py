import random
from words import words
import string

# Some of the words in the dictionary have spaces and dashes in them.
# And we can't guess spaces and dashes. 
# So we create a function that doesn't stop running until a valid word without spaes and dashes is gotten.



def get_valid_word(words):       
    word = random.choice(words)      # randomly chooses something from the list
    while "_" in word or " " in word:  # This enables the computer to keep repeating the process until a valid word is found.
        word = random.choice(words)

    return word.upper()
        
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   # This variable keeps track of all the letters in the word the computer guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # To keep track of what the user has guessed

    lives = 6
 

    # To get input from the user
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (i.e W _ R D)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("letter is not in the word")

        elif user_letter in used_letters:
            print("You have already used that charater. Please try again.")

        else: 
            print("Invalid character. Please try again!")   

    # Gets here when len(word_letters) == 0  OR when lives == 0    
    if lives == 0:
        print("You died, sorry. The word is", word)
        
    else:
        print("You guessed the word", word, "correctly!!")
        

hangman()
