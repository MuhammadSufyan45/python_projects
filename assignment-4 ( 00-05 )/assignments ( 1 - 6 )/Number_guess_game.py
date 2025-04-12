import random

top_of_range = input("Type a maximum number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Type a number greater than 0") 
        quit()

else:
    print("Please type a number")
    quit()

random_num = random.randint(0,top_of_range)
guessess = 0

while True : 
    guessess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
     user_guess = int(user_guess) 
    else:
        print("Please type a number")
        continue

    if user_guess == random_num : 
        print("You got it!")
        break
    elif user_guess > random_num :
        print("You were above the random number")
    else : 
        print("You were below the random number")


print("You got it in", guessess, "guessess.")
   