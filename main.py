from Topics import Classic, Movies, Video_games, Countries, Hangman_parts
import random


# Chooses a random word from the topic that the user entered
def random_word(topic):
    if topic == "CLASSIC":
        word = random.choice(Classic)
        return play(word.upper())
    elif topic == "MOVIE":
        word = random.choice(Movies)
        return play(word.upper())
    elif topic == "VIDEO GAME":
        word = random.choice(Video_games)
        return play(word.upper())
    elif topic == "COUNTRY":
        word = random.choice(Countries)
        return play(word.upper())
    else:
        # This allows the user to enter a topic again because the first attempt was invalid
        print("\nYou entered a invalid Topic, try again.")
        main()


def play(word):
    guessed = False
    guessed_letters = []
    guessed_words = []
    hidden_word = "*" * len(word)
    lives = 6
    print(Hangman_parts[lives])
    print(f"Secret word: {hidden_word}")
    print(f"Letters in word: {len(word)}")
    print(f"Lives = {lives}")
    while not guessed and lives > 0:
        user_guess = input("\nEnter a guess, this can either be a letter or a word: ").upper().strip()
        # User entered a single letter guess
        if len(user_guess) == 1:
            # Checks if the user guess is in guessed letters
            if user_guess in guessed_letters:
                print(f"You already guessed this letter: {user_guess}")
            # Checks if the user guess is not in the word
            elif user_guess not in word:
                guessed_letters.append(user_guess)
                lives -= 1
                print(f"Sorry but {user_guess} is not in the word")
            # Means the user guess is in the word
            else:
                print(f"Correct {user_guess} is in the word")
                guessed_letters.append(user_guess)
                # The list comprehension below reveals the correct letters the user guessed
                word_list = list(hidden_word)
                spot = [i for i, letter in enumerate(word) if letter == user_guess]
                for i in spot:
                    word_list[i] = user_guess
                hidden_word = "".join(word_list)
                if "*" not in hidden_word:
                    guessed = True
        # User entered a guess the length of the word
        elif len(user_guess) == len(word):
            # Checks if the user guess is in guessed words
            if user_guess in guessed_words:
                print(f"You already guessed this word: {user_guess}")
            # Checks if the user guess is not the word
            elif user_guess != word:
                guessed_words.append(user_guess)
                lives -= 1
                print(f"Sorry but {user_guess} is not the word")
            # Means the user guessed the word
            else:
                hidden_word = word
                guessed = True
        # Users guess is invalid
        else:
            print("You entered a invalid guess.")
        print(Hangman_parts[lives])
        print(f"hidden word: {hidden_word}")
        print(f"Letters in word: {len(word)}")
        print(f"lives remaining: {lives}")
        print(f"Guessed letters: {guessed_letters}")
        print(f"Guessed words: {guessed_words}")
    if lives == 0:
        print("\n                    You died")
        print(f"Sorry but you ran out of lives, the word was: {word}")
    else:
        print(f"\nCongratulation you guessed the word: {word}")
    answer = input("\nWould you like to play again, Yes(Y)/No(N): ").upper().strip()
    if answer[0] == "Y":
        topic_again = input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper().strip()
        random_word(topic_again)


def main():
    global topic
    topic = input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper().strip()
    random_word(topic)


# This should be the first thing you see when the game starts
print("\nLet's play Hangman!!")
main()