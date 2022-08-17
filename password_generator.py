# Ask the user how long they want their password to be and how many letters and numbers they want in their password
# Have a mix of upper and lowercase letters, as well as numbers and symbols
# The password should be a minimum of 6 characters long

import random
import string


# string for the password
def password():
    while True:
         # We create a bunch of strings containing all possible characters that we can use for our password
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        all = ""
        
        if letters:
            all += letters
        if numbers:
            all += numbers
        if symbols:
            all += symbols

        password1 = ""
        password2 = ""
        password3 = ""

        length_password = input("How long do you want your password to be: ")
        if length_password.isdigit():
            length_password = int(length_password)
            if length_password < 6:
                print("Sorry, there should be a minimum of 6 characters")
                continue
            else:
                length_letters = input("How many letters do you want in the password: ")
                if length_letters.isdigit():
                    length_letters = int(length_letters)
                    for i in range(1):
                        password1 = password1, "".join(random.sample(letters, length_letters))
                    length_numbers = input("How many numbers do you want in your password: ")
                    if length_numbers.isdigit():
                        length_numbers = int(length_numbers)
                        for i in range(1):
                            password2 = password2, "".join(random.sample(numbers, length_numbers))
                        length_symbols = input("How many symbols do you want in your password: ")
                        if length_symbols.isdigit():
                            length_symbols = int(length_symbols)
                            for i in range(1):
                                password3 = password3, "".join(random.sample(symbols, length_symbols))
                            all = password1 + password2 + password3

                            total = length_letters + length_numbers + length_symbols
                            

                            # To check if the total number is not greater than the length of the password the user wants
                            if total > length_password:
                                print("Invalid! Your numbers don't add up.")
                                continue
                            elif total < length_password:
                                print("Invalid! Your numbers don't add up.")
                                continue
                            else:
                                number_of_passwords = input("How many passwords do you want? ")
                                if number_of_passwords.isdigit():
                                    number_of_passwords = int(number_of_passwords)
                                    for i in range(number_of_passwords):
                                        try:
                                            password = "".join(random.sample(all, total))
                                            print(str(password))
                                        except:
                                            print("Please let the total length of your password be equal to 6")
                                    print("Here are (is) your", number_of_passwords, "password(s).")
                                else:
                                    print("Please type  a number")
                                    break
                        else:
                            print("Please type  a number")
                            break
                    else:
                        print("Please type  a number")
                        break
                else:
                    print("Please type  a number")
                    break

        else:
            print("Please type a number!")
            continue
            


password()



