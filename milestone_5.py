import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.initialize_game()

    def initialize_game(self):
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            self.handle_correct_guess(guess)
        else:
            self.handle_incorrect_guess(guess)

    def handle_correct_guess(self, guess):
        print(f"Good guess! {guess} is in the word")
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

        if not '_' in self.word_guessed:
            self.display_result("Congratulations. You won the game!")

    def handle_incorrect_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")
        
        if self.num_lives == 0:
            self.display_result(f"You lost! The correct word was: {self.word}")

    def display_current_word(self):
        print(f"Current word: {' '.join(self.word_guessed)}")

    def display_result(self, message):
        print(message)

    def ask_for_input(self):
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
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        game.ask_for_input()
        if game.num_lives == 0 or not '_' in game.word_guessed:
            break

word_list = ["apple", "banana", "orange", "grapes", "mango"]
play_game(word_list)

#TODO add docstrings