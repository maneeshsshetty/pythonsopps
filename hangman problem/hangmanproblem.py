import random
import os
def load_words():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "file.txt")
    with open(file_path, "r") as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return words
def choose_word(words):
    return random.choice(words)

def play_game(word):
    guessed_letters = set()
    chances = 6

    print("\nWelcome to Hangman!")
    while chances > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display.strip())

        if all(letter in guessed_letters for letter in word):
            print("You won! The word was:", word)
            return

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            chances -= 1
            print("Incorrect!")
            print(f"You have {chances} chances left.")

    print("Game Over! The word was:", word)
def main():
    words = load_words()

    while True:
        word = choose_word(words)
        play_game(word)

        again = input("\n Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


main()