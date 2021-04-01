from english_words import words
import random


def main():

    tries = 0
    display_word = ''

    # Choose word
    print('\nStep 1')
    random_word = random.choice(words).upper()

    # Display word
    print('\nStep 2')
    for letter in random_word:
        display_word += '_'

    print(display_word)
    print(random_word)

    game_running = True
    while game_running:

        guesses = []
        updated_display_word = ''

        # User guess
        print('\nStep 3')
        user_guess = input('Guess the word or letter: ')
        user_guess = user_guess.upper()

        # Store user guess
        guesses.append(user_guess)

        # Conditional == word
        # Game end
        print('\nStep 4')
        if user_guess == random_word:
            print(random_word)
            print('Win')

            # Try again

        # Conditional == letter
        print('\nStep 5')
        if user_guess in random_word:

            letter_occurence = []
            # Find all occurences and update the display
            # FIX
            print('Step 5.1')

            for index, element in enumerate(random_word):
                if element == user_guess:
                    letter_occurence.append(index)

            for index, element in enumerate(display_word):
                if index in letter_occurence:
                    display_word += user_guess
                else:
                    display_word += '_'

            # Game end
            print('Step 5.2')
            if '_' not in display_word:
                print('Win')

            # Print updated word
            print('Step 5.3')
            print(display_word)

        elif user_guess not in random_word:
            tries += 1
            print(f'Tries: {tries}')
            print('Letter not in word\n')
            continue


if __name__ == '__main__':
    main()
