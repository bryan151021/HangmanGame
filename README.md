# HangmanGame
This is a simple Hangman game written in python that will ask the user to enter one of the following four topics to play in: **Classic**, **Movie**, **Video Game**, or **Country**. 

## There are three main functions in this code:
- `random_word`: Chooses a random word from the list that the user entered                          
- `play`: The main interface that the user will see/use, user will be guessing the word here  
- `main`: Allows the user to enter the topic they will like to play in

## Description of the game:
When you start the game, you will be asked to enter a topic that you would like to play in. The code will select a random word from the topic that the user entered then they will be asked to enter a guess, this can either be a letter or a word. You will be given six lives to guess the word, for every incorrect attempt, the code will take one life away from the user, and when you have zero lives left, the game will end. However, you will be given the chance to play again at the end. 

## How users can get started:
You will need to have an IDE installed to run the code, like **Pycharm**, and **Git** installed in your terminal to clone/copy my code onto your computer. Start by cloning my repository, to do this click on the green rectangle that says "`<> Code`", and copy the **HTTPS URL**. Then open up your terminal, you can download a free one online if you don't have any, like **Cygwin**, or use the one that came with your computer. Once open, type `git clone` and paste the URL that you copied earlier. Then type `ls -la` or `ls` to check if the folder downloaded on your computer, then change the directory to the folder's name, to do this type `cd HangmanGame`(folder name). Then type `ls -la` or `ls` again to see if all the files were downloaded inside the folder. Then use your IDE to open up the folder, and you should be able to play the game.

## Where users can get help and contribution:
Im currently the only person working on this project, so if you need any help you can contact me through this email, bmw10420@gmail.com. I will set up a contribution section later on. As of right now the code should work perfectly fine so no changes are needed. If some changes would be made, it would be some new features to the game. 

## Examples of what some code/lines will print:
- Checks the user guess to see if it's in the word, if it's not in the word, if it's a invalid guess, and more:
```
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
 ```
### `Output:`  ![Untitled 5](https://user-images.githubusercontent.com/119261711/222999662-d3a54520-7b00-4168-88a7-59ab9e2dda44.png)

----
- Tells the user to enter one of the four topics:
```
def main():
    global topic
    topic = input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper().strip()
    random_word(topic)
```
### `Output:` ![Untitled 3](https://user-images.githubusercontent.com/119261711/222940642-527a5cb8-2273-4521-a214-2d99e9bd7f35.png)

----
- Prints the information the user needs to see, like how many lives he has left, the guessed letters he has entered, etc.
```
        print(Hangman_parts[lives])
        print(f"hidden word: {hidden_word}")
        print(f"Letters in word: {len(word)}")
        print(f"lives remaining: {lives}")
        print(f"Guessed letters: {guessed_letters}")
        print(f"Guessed words: {guessed_words}")
```
### `Output:` ![Untitled 4](https://user-images.githubusercontent.com/119261711/222940726-dd64dc7e-51ce-49d2-bb68-4685e5a9a261.png)
