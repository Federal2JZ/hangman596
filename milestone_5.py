import random


class Hangman:
    """
    Hangman class represents the Hangman game.

    Attributes:
    - word_list (list): A list of words for the game.
    - word (str): The randomly selected word to be guessed.
    - word_guessed (list): List representing the current state of the guessed word.
    - num_letters (int): Number of unique letters in the word.
    - num_lives (int): Number of lives the player has.
    - list_of_guesses (list): List of guessed letters.

    Methods:
    - initialize_game(): Initialize the game with a random word.
    - check_guess(guess): Check if the guessed letter is in the word.
    - handle_correct_guess(guess): Handle the case when the guessed letter is correct.
    - handle_incorrect_guess(guess): Handle the case when the guessed letter is incorrect.
    - display_current_word(): Display the current state of the guessed word.
    - display_result(message): Display the game result message.
    - ask_for_input(): Ask the user to input a letter and process the guess.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game.

        Parameters:
        - word_list (list): A list of words for the game.
        - num_lives (int): Number of lives the player has (default is 5).
        """
        self.word_list = word_list
        self.initialize_game()

    def initialize_game(self):
        """Initialize the game with a random word."""
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess (str): The guessed letter.
        """
        guess = guess.lower()

        if guess in self.word:
            self.handle_correct_guess(guess)
        else:
            self.handle_incorrect_guess(guess)

    def handle_correct_guess(self, guess):
        """
        Handle the case when the guessed letter is correct.

        Parameters:
        - guess (str): The correct guessed letter.
        """
        print(f"Good guess! {guess} is in the word")
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

        if not '_' in self.word_guessed:
            self.display_result("Congratulations. You won the game!")

    def handle_incorrect_guess(self, guess):
        """
        Handle the case when the guessed letter is incorrect.

        Parameters:
        - guess (str): The incorrect guessed letter.
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")
        
        if self.num_lives == 0:
            self.display_result(f"You lost! The correct word was: {self.word}")

    def display_current_word(self):
        """Display the current state of the guessed word."""
        print(f"Current word: {' '.join(self.word_guessed)}")

    def display_result(self, message):
        """
        Display the game result message.

        Parameters:
        - message (str): The result message.
        """
        print(message)

    def ask_for_input(self):
        """Ask the user to input a letter and process the guess."""
        while True:
            self.display_current_word()
            guess = input("Enter a single letter: ")

            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                if self.num_lives == 0 or not '_' in self.word_guessed:
                    break

def play_game(word_list):
    """
    Play the Hangman game.

    Parameters:
    - word_list (list): A list of words for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        game.ask_for_input()
        if game.num_lives == 0 or not '_' in game.word_guessed:
            break

word_list = ["apple", "banana", "orange", "grapes", "mango"]
play_game(word_list)