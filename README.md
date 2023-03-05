# HangmanGame
This is a simple Hangman game written in python that will give the user the chance to choose one of the following topics to play in: **Classic**, **Movie**, **Video Game**, or **Country**. 

----
### There are three main functions in this code:
- `random_word`: Chooses a random word from the list that the user entered                          
- `play`: The main interface that the user will see/use, user will be guessing the word here  
- `main`: Allows the user enter the topic they will like to play in
----
### Description of the game:
When you start the game, the user will be asked to enter a topic they would like to play in. The code will select a random word from the topic that the user entered then they will be asked to enter a guess, this can either be a letter or a word. You will be given six lives to guess the word, for every incorrect attempt, the code will take one life away from the user, and when you have zero lives left, the game will end. However, you will be given the chance to play again at the end. 

----
### How users can get started:
You will need to have an IDE installed to run the code, I used Pycharm. Start by creating a new project and naming it. Then create two files, one file will be named Topics and will have the lists of words for each topic and the parts of the hangman. The other file will be named main and it will contain the whole code to run the game. Then insert the code into their proper files and after that, you should be able to play the game.

----
### Where users can get help and contribution:
Im currently the only person working on this project, so if you need any help you can contact me through this email, bmw10420@gmail.com. I will set up a contribution section later on. As of right now the code should work perfectly fine so no changes are needed. If some changes would be made, it would be some new features to the game. 

----
### Examples of the output of some of the code/lines:
- Chooses a random word from the list the topic the user entered:
```
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
 ```
`Output:`  ![Untitled](https://user-images.githubusercontent.com/119261711/222940369-59bad894-5dfc-4e76-8f8e-8f6cc10b44ee.png)

- Tells the user to enter one of the four topics:
```
def main():
    global topic
    topic = input("Enter one of the following topic's that you will like to play: Classic, Video Game, Country, or Movie: ").upper().strip()
    random_word(topic)
```
`Output:` ![Untitled 3](https://user-images.githubusercontent.com/119261711/222940642-527a5cb8-2273-4521-a214-2d99e9bd7f35.png)

- Prints the information the user needs to see, like how many lives he has left, the guessed letters he has entered, etc.
```
        print(Hangman_parts[lives])
        print(f"hidden word: {hidden_word}")
        print(f"Letters in word: {len(word)}")
        print(f"lives remaining: {lives}")
        print(f"Guessed letters: {guessed_letters}")
        print(f"Guessed words: {guessed_words}")
```
`Output:` ![Untitled 4](https://user-images.githubusercontent.com/119261711/222940726-dd64dc7e-51ce-49d2-bb68-4685e5a9a261.png)



