import random

N_NUMBERS : int = 10
MIN_NUMBER : int = 1
MAX_NUMBER : int = 100

def main():
    for i in range(N_NUMBERS):
        print(random.randint(MIN_NUMBER, MAX_NUMBER) , end=" ")

if __name__ == "__main__":
        main()