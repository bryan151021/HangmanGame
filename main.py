from Topics import Classic, Movies, Video_games, Countries, Hangman_parts
import random


# Chooses a random word from the topic the user entered
def random_word(topic):
    topic = topic.strip()
    global count
    if topic == "CLASSIC":
        word = random.choice(Classic)
        word = word.upper()
        count += 0
        if answer[0] == "Y":
            count = 0
        return play(word)
    elif topic == "MOVIE":
        word = random.choice(Movies)
        word = word.upper()
        count += 0
        return play(word)
    elif topic == "VIDEO GAME":
        word = random.choice(Video_games)
        word = word.upper()
        count += 0
        return play(word)
    elif topic == "COUNTRY":
        word = random.choice(Countries)
        word = word.upper()
        count += 0
        return play(word)
    else:
        # This allows the user to input the topic again because the first attempt was invalid
        print("\nYou entered a invalid Topic, try again.")
        global again
        again = (input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper())
        count += 1
        random_word(again)


def play(word):
    guessed = False
    guessed_letters = []
    guessed_words = []
    hidden_word = "*" * len(word)
    lives = 6
    # Decides whether to use the first topic the user entered or the second one
    b = topic if count == 0 else again
    print(f"\nTopic: {b.strip()}", end='')
    print(Hangman_parts[lives])
    print(f"Secret word: {hidden_word}")
    print(f"Lives = {lives}")
    while not guessed and lives > 0:
        user_guess = input("\nEnter a guess, this can either be a letter or word: ").upper()
        # user guess is a letter
        if len(user_guess) == 1:
            # checks if user guess is in guessed letters
            if user_guess in guessed_letters:
                print(f"You already guessed this letter: {user_guess}")
            # checks if user guess is not in the word
            elif user_guess not in word:
                guessed_letters.append(user_guess)
                lives -= 1
                print(f"Sorry but {user_guess} is not in the word")
            # means user guess is in the word
            else:
                print(f"Correct {user_guess} is in the word")
                guessed_letters.append(user_guess)
                # this list comprehension below reveal the correct user guesses
                word_list = list(hidden_word)
                spot = [i for i, letter in enumerate(word) if letter == user_guess]
                for i in spot:
                    word_list[i] = user_guess
                hidden_word = "".join(word_list)
                if "*" not in hidden_word:
                    guessed = True
        # user guess is a word
        elif len(user_guess) == len(word):
            # checks if user guess is in guessed words
            if user_guess in guessed_words:
                print(f"You already guessed this word: {user_guess}")
            # checks if user guess is not in the word
            elif user_guess != word:
                guessed_words.append(user_guess)
                lives -= 1
                print(f"Sorry but {user_guess} is not the word")
            # means user guess is in word
            else:
                hidden_word = word
                guessed = True
        # user guess is invalid
        else:
            print("You entered a invalid guess.")
        b = topic if count == 0 else again
        print(f"\nTopic: {b.strip()}", end='')
        print(Hangman_parts[lives])
        print(f"hidden word: {hidden_word}")
        print(f"lives remaining: {lives}")
        print(f"Guessed letters: {guessed_letters}")
        print(f"Guessed words: {guessed_words}")
        if lives == 0:
            print("\n                 You died")
            print(f"Sorry but you ran out of lives, the word was: {word}")
        elif guessed:
            print(f"\n Congratulation you guessed the word: {word}")
        else:
            continue


def main(topic):
    random_word(topic)
    global answer
    answer = input("\nWould you like to play again, Yes(Y)/No(N): ").upper()
    if answer[0] == "Y":
        topic_again = input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper()
        random_word(topic_again)


# This should be the first thing you see and this starts the game
print("\nLet's play Hangman!!")
topic = input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper()
count = 0
main(topic)
