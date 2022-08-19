# Here the user picks a random number, the computer guesses which number the user picked.
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) 
        if guess < random_number:
            print("Guess lower than the number.")
        elif guess > random_number:
            print("Guess higher than the number.")

    print("Congrats, you got it!")
         

guess(100)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:          
            guess = random.randint(low, high)
        else:
            guess = low  # Could also be high, because low = high 

        feedback = input(f'Is {guess} too high (H), too low(L), or correct(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("The computer guessed right!")

computer_guess(1987)
