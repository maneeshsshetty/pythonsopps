import random

def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])


def count_cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0

    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1

    return cows, bulls


def play_game():
    secret_number = generate_number()
    guesses = 0

    print("Welcome to the Cows and Bulls Game!")

    while True:
        guess = input("Enter a 4-digit number (no repeated digits): ")


        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input! Enter 4 unique digits.")
            continue

        guesses += 1
        cows, bulls = count_cows_and_bulls(secret_number, guess)

        print(f"{cows} cows, {bulls} bulls")

        if cows == 4:
            print("Congratulations! You guessed the correct number!")
            print(f"It took you {guesses} guesses.")
            break

play_game()
