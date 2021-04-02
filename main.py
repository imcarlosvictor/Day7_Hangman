from english_words import words
from typing import List
import random


def pick_random_word(word_in_underscore) -> str:
    """AI picks a random word from the word module.

    Args:
        word_in_underscore - placeholder variable for chosen word.

    Returns:
        str: chosen word by the AI.

    """

    # Choose word
    chosen_word = random.choice(words).upper()

    # Add an underscore to the word placeholder
    for letter in chosen_word:
        word_in_underscore.append('_')

    # Display word for user to see
    display_word = ' '.join(word_in_underscore)
    print(chosen_word)

    return chosen_word, display_word


def play_again(flag: bool) -> bool:
    """Asks user if he/she wants to play again.

    Args:
        flag - Flag of loop

    Returns:
        bool: True for continue, False otherwise.

    """

    try_again = True
    while try_again:

        user_play_again = input('Play again? (y/n): ')

        if user_play_again == 'n':
            print('\nEnding Game...')
            flag = False
            return flag
            # try_again = False
        elif user_play_again == 'y':
            print('Starting new game...\n')
            flag = True
            return flag
            # try_again = False
        elif user_play_again != 'n' or user_play_again != 'y':
            print("Enter either 'y' or 'n'")


def main():

    store_guesses: List[str] = []
    wrong_guesses: int = 0

    word_to_underscore: List[str] = []  # The word in underscores

    random_word, display_word = pick_random_word(
        word_to_underscore)  # Chooses a random word

    game_running = True
    while game_running:

        # Check if all underscores have been converted into a letter
        if '_' not in word_to_underscore:
            print('\nWin')

            # Determine whether the player wants to play again or not
            game_running = play_again(game_running)

            # Value of the flag determines whether the game ends or restarts
            if not game_running:
                break
            elif game_running:
                wrong_guesses = 0

                word_to_underscore.clear()  # Reset list

                # Choose a new word for the new game
                random_word, display_word = pick_random_word(
                    word_to_underscore)
                continue

        # Display updated word
        print(' '.join(word_to_underscore))

        # Check if wrong_guesses == 5
        if wrong_guesses == 6:
            print(f'Tries: {wrong_guesses}/6')
            print(f'Word is: {random_word}')

            # Determine whether the player wants to play again or not
            game_running = play_again(game_running)

            # Value of the flag determines whether the game ends or restarts
            if not game_running:
                break
            elif game_running:
                wrong_guesses = 0

                word_to_underscore.clear()  # Reset list

                # Choose a new word for the new game
                random_word, display_word = pick_random_word(
                    word_to_underscore)
                continue

        # Ask for user's guess
        user_guess: str = input('Guess the word or letter: ')
        user_guess = user_guess.upper()

        store_guesses.append(user_guess)  # Store the user's guesses

        if user_guess == random_word:
            # If the guess is a word
            print(random_word)
            print('Win')

            # Determine whether the player wants to play again or not
            game_running: bool = play_again(game_running)

            # Value of the flag determines whether the game ends or restarts
            if not game_running:
                break
            elif game_running:
                wrong_guesses = 0

                word_to_underscore.clear()  # Reset list

                # Choose a new word for the new game
                random_word, display_word = pick_random_word(
                    word_to_underscore)
                continue

        if user_guess in random_word:
            # If the guess is a  letter

            letter_occur_index: List[int] = []  # Keeps track of the

            # Find all occurences and store the index
            for index, element in enumerate(random_word):
                if element == user_guess:
                    letter_occur_index.append(index)

            # Iterate and change underscore to letter guessed
            for index, element in enumerate(word_to_underscore):
                if index in letter_occur_index:
                    word_to_underscore[index] = user_guess

        elif user_guess not in random_word:
            wrong_guesses += 1
            print(f'Tries: {wrong_guesses}')
            print('Letter not in word\n')

    print('Thank you for playing.')


if __name__ == '__main__':
    main()
