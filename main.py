import random

class WordGame:
    def __init__(self):
        self.words: list[str] = []
        self.word: str = ""
        self.scrambled_word: str = ""
        self.attempts: int = 0
        self.load_words()

    def load_words(self) -> None:
        try:
            with open("words.txt", "r") as file:
                self.words: list[str] = [word.strip() for word in file]
            if not self.words:
                print("File is empty. Exiting program.")
                quit()
        except FileNotFoundError:
            print("File not found!")
            quit()

    def run_game(self) -> None:

        # Create a random number between 0, len(words)
        i: int = random.randint(0, len(self.words) - 1)

        # Assign that number as the word words[number]
        self.word: str = self.words[i]

        # Scramble the word
        self.scrambler()

        # Start the game
        self.guesser()


    def scrambler(self) -> None:
        # Create a list of chars
        c_list: list[str] = list(self.word)

        while True:
            # Shuffle chars in list
            random.shuffle(c_list)

            # Join the chars in list into string
            self.scrambled_word: str = "".join(c_list)

            # Ensure the word is scrambled
            if self.scrambled_word != self.word:
                break

        # Print the scrambled word
        print(f"Guess the word: {self.scrambled_word}")

    def guesser(self) -> None:
        # Count for every guess
        self.attempts: int = 0

        while True:
            # Get user input for a guess
            guess: str = input("Answer (/quit to exit): ")

            # Allow the player to quit
            if guess.lower() == '/quit':
                print("Exiting the game")
                break
            # Compare the guess and the original list[number]
            if not guess == self.word:
                self.attempts += 1
                print(f"Wrong guess! Continue. ({self.attempts} attempts)")
                continue
            # End the game if player is correct and print amount of guesses
            else:
                self.attempts += 1
                print(f"Correct! You win! ({self.attempts} attempts)")
                break

def main() -> None:
    WordGame().run_game()

if __name__ == "__main__":
    main()