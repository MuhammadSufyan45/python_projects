import random

def main():

    secret_num: int = random.randint(1,99)

    print("Welcome to the Number Guessing Game! I am guessing of a number between 1 and 99.")

    guess  = int(input("Make a guess: "))

    while guess != secret_num:
        if guess < secret_num:
            print("Your Guess Is Too low!")
        else:
            print("Your Guess Is Too High!")

        print()

        guess = int(input("Make a new guess: "))
    
    if guess == secret_num:
        print("Congratulations! You have guessed the number correctly!: " + str(secret_num))


if __name__ == "__main__":
    main()