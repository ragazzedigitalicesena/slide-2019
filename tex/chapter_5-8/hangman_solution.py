# Importa il modulo random - Parte 1
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# Da fare - Parte 1
correctLetters = ''
missedLetters = ''
wordsString = 'Ragazze Digitali Cesena Giugno'
words = wordsString.split()
# ! Sarebbe stato uguale fare wordsString = 'Ragazze Digitali Cesena'.split()

def getRandomWord(wordList):
    # Da fare - Parte 2
    wordIndex = random.randint(0, len(words) - 1) # Perche' -1 ???
    return wordList[wordIndex]

secretWord = getRandomWord(words)
# ! Ho utilizzato getRandomWord(words) dopo aver definito la funzione !

def displayBoard(missedLetters, correctLetters, secretWord):
    # Da fare - Parte 3
    numberOfMissedLetters = len(missedLetters)
    print(HANGMAN_PICS[numberOfMissedLetters])
    print('Lettere sbagliate' + missedLetters)
    # Da fare - Parte 4
    guessedLetters = []
    for i in range(len(secretWord)) :
        if secretWord[i] in correctLetters:
            guessedLetters.append(secretWord[i])
        else:
            guessedLetters.append('_')
    print(guessedLetters)



def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

# def playAgain():
    # Da fare - Parte 5

print('H A N G M A N')

gameIsDone = False

play = True

while play:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            play = False
