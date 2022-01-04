import random

words = ['act', 'air', 'age', 'bag', 'cap', 'map', 'area', 'baby', 'card', 'dish', 'exam', 'good', 'boards', 'chair', 'count', 'facts', 'green', 'house']

hangman_graphics = ['_',
                    '__',
                    '__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ '                
                    ]

number_mistakes = 0
letters_guessed = []
number_mistakes_allowed = len(hangman_graphics)
word = random.choice(words)
letters_word = list(word)
wrong_letters = []

print()
print('The word has {} letters'.format(len(letters_word)))

while number_mistakes < number_mistakes_allowed:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print('{}, '.format(letter), end='')
    print()
    print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes))
    letter_user = input('Enter a letter --> ')

    while letter_user in letters_guessed or letter_user in wrong_letters:
        print()
        print('You have already entered this letter, enter another one')
        letter_user = input('Enter a letter --> ')

    if letter_user not in letters_word:
        number_mistakes += 1
        wrong_letters.append(letter_user)

    print()
    print('Word: ', end='')

    for letter in letters_word:
        if letter_user == letter:
            letters_guessed.append(letter_user)
    
    for letter in letters_word:
        if letter in letters_guessed:
            print(letter + ' ', end='')
        else:
            print('_ ', end='')

    print()
    if number_mistakes:
        print(hangman_graphics[number_mistakes - 1])
    print()
    print('-------------------------------------------')

    if len(letters_guessed) == len(letters_word):
        print()
        print('YOU WOOOON!!!')
        break

if number_mistakes == number_mistakes_allowed:
    print()
    print('YOU LOST! TRY AGAIN!')   
