import random

def choose_random_word(word_list):
    return random.choice(word_list)

def get_user_guess():
    return input("Enter a single letter: ")

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def print_feedback(valid_guess):
    if valid_guess:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

def main():
    # Create a list containing the names of your 5 favorite fruits.
    favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
    
    # Print out the word list
    print("Word List:", favorite_fruits)

    # Choose a random word from the list
    word = choose_random_word(favorite_fruits)
    print(word)

    # Get user guess
    guess = get_user_guess()

    # Validate and print feedback
    valid_guess = is_valid_guess(guess)
    print_feedback(valid_guess)

if __name__ == "__main__":
    main()