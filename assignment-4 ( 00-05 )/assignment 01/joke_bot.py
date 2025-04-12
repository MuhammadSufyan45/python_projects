PROMPT: str = "What do you want ?: "
JOKE: str = "Here's a joke for you: Why Eggs don't tell jokes to eachother? bcz they might crack each other up"
SORRY: str = "Sorry I only tell jokes"

def main():
    print("Hello! I am a joke bot")
    print("Write exit to quit if you want quit anytime ")
    while True:
        user_input = input(PROMPT).strip().lower()

        if user_input == "exit":
            break
        if "joke" in user_input:
            print(JOKE)
        else:
            print(SORRY)

if __name__ == "__main__":
    main()