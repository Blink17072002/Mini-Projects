print("Welcome to my computer quiz!")

# To ask the user if he wants to play the game
playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the president of the United States? ")
if answer.lower() == "joe biden":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does IPO stand for? ")
if answer.lower() == "Initial Public Offering":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What year are we in? ")
if answer.lower() == "2022":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score)/5 + " questions correct!")

