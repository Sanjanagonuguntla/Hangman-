# Hangman-


--> A Hangman Game On Python is about guessing letters (A-Z) to form the words. If the player guesses the right letter that is within the word, the letter appears at its correct position. The user has to guess the correct word until a man is hung, then the game is over.

--> This is a Python script of the classic game “Hangman”. The word to guess is represented by a row of dashes. If the player guess a letter which exists in the word, the script writes it in all its correct positions.  The player has 10 turns to guess the word. You can easily customize the game by changing the variables

--> The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.

--> The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.

--> When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over.
  
--> For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letter word.
