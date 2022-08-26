from random import randint, randrange, sample
import string

top_of_range = input("What number do you want to be your top of range? ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range < 2:
        print("Please type a number greater than 2.")
else:
    print("Invalid input! Pease type a number")

# Create a random list of numbers between 0 and the user's top_of_range with a difference of 2 between each number
k = input("How many numbers do  you want the computer to pick in the list? ")

if k.isdigit():
    k = int(k)

    if k > top_of_range/2:
        print("Invalid input! Your numbers do not add up. Please type a number less than or equal to half of your top of range.")
    else:
        # This is where most of the code for this whole programme is 
        numbers = sample(range(0, top_of_range, 2), int(k))
        print(numbers, "\n")   

        # Splitting the list into two parts
        middle_index = k // 2  # To get an integer (floor() function)

        sub_array = len(numbers)

        while sub_array > 0:

            # Split the list (numbers) from starting index up to middle index in first half
            first_half = numbers[:middle_index]
            print(f"This is the first half of the list: {first_half} \n")

            # Split the list (numbers) from the middle index to the ending point in the second half
            second_half = numbers[middle_index:]
            print(f"This is the second half of the list: {second_half} \n")
            user_num = input(f"Type a number between 0 and {top_of_range}: ")

            if user_num.isdigit():
                user_num = int(user_num)
                if user_num > top_of_range:
                    print("Invalid input! Please try again")
                    continue
                else:
                    if user_num == numbers[middle_index - 1]:
                        print("Congrats! You won the game")
                        break
                    
                    else:
                        middle_first_half_index = len(first_half) // 2
                        middle_second_half_index = len(second_half) // 2
                        if user_num in first_half:
                            if user_num == first_half[middle_first_half_index - 1]:
                                print("Congrats! You won the game!")
                                break
                            else:
                                middle_first_half_of_first_half_index = len(first_half) // 4
                                first_half_of_first_half = first_half[:middle_first_half_of_first_half_index]
                                second_half_of_first_half = first_half[middle_first_half_of_first_half_index:]

                                if user_num == first_half_of_first_half[middle_first_half_of_first_half_index - 1]:
                                    print("Congrats! You won the game")
                                    break
                                elif user_num == second_half_of_first_half[middle_first_half_of_first_half_index - 1]:
                                    print("Congrats! You won the game")
                                    break
                                

            else:
                print("Invalid input! Please type a number.")
                continue
            sub_array = len(second_half)
            middle_index == sub_array // 2
            numbers = second_half

        else:
            print("Sorry, length of sub-array is 0. Game Over!")
else:
    print("Invalid input! Pease type a number")
