import random
import os
import time
from itertools import (takewhile, repeat)

wordfile = 'wordLists/text.txt'
wordlist = open(wordfile, 'r')


# Ansi escape codes for changing text colour based on asnwers
class colours:
    RED = '\u001b[31m'
    AMBER = '\u001b[33m'
    GREEN = '\u001b[32m'
    RESET = '\u001b[0m'


# Work out the score for the player
def finalScore():
    end = time.time()
    global score, timeTaken
    timeTaken = round(end - start)
    maxScore = 100000
    scoreMultiplier = {
        6: 1.1,
        5: 1.3,
        4: 1.5,
        3: 1.9,
        2: 2.5,
        1: 5
    }
    score = maxScore / timeTaken
    score *= scoreMultiplier[attempts]
    score = round(score)


# Count lines in file to allow for any wordlist
def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024)
                       for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen)
    f.close()


# Find a word from the wordlist
def findWord():
    global word, letters
    wordlistReadLines = wordlist.readlines()
    wordLine = random.randint(0, (rawincount(wordfile)-1))
    word = wordlistReadLines[wordLine]
    word = word.replace('\n', '')
    letters = list(word)


# Allow user to guess the word
def guessWord():
    global guess, attempts
    correctLen = False
    while correctLen == False:
        guess = input().lower()
        if len(guess) > 5:
            print('Guess Too long, try again')
        elif len(guess) < 5:
            print('Guess too short, try again')
        else:
            correctLen = True
    guess = list(guess)
    attempts += 1


# Check to see which letters of the word is correct
def checkWord():
    global gameComplete, wordAttempts
    checkWord = letters[:]
    correct = 0
    outcome = []
    for x in guess:
        if x in word:
            correctLetter = False
            correctPlace = False
            for y in checkWord:
                if correctPlace == False and correctLetter == False:
                    if x == y:
                        if guess.index(x) == checkWord.index(y):
                            outcome.append(
                                f'{colours.GREEN}{x}{colours.RESET}')
                            correctPlace = True
                            guess[guess.index(x)] = '!'
                            correct += 1
                            if x in lettersNotUsed:
                                lettersNotUsed.remove(x)
                        else:
                            if checkWord.count(y) > 1:
                                checkWord[checkWord.index(y)] = y+'!'
                            else:
                                outcome.append(
                                    f'{colours.AMBER}{x}{colours.RESET}')
                                correctLetter = True
                                guess[guess.index(x)] = '!'
                                if x in lettersNotUsed:
                                    lettersNotUsed.remove(x)
        else:
            outcome.append(f'{colours.RED}{x}{colours.RESET}')
            if x in lettersNotUsed:
                lettersNotUsed.remove(x)
    print(''.join(outcome))
    wordAttempts.append(''.join(outcome))

    if correct == 5:
        gameComplete = True


# Storing the start screen as a function to make code more readable
def startScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
                    ____         
   _________  ___  / / /__  _____
  / ___/ __ \/ _ \/ / / _ \/ ___/
 (__  ) /_/ /  __/ / /  __/ /    
/____/ .___/\___/_/_/\___/_/     
    /_/                          
                                
Welcome to SPELLER by xhemals
You have 6 attempts to guess the word
{colours.GREEN}Green means you have the letter in the right space
{colours.AMBER}Amber means the letter is in the word
{colours.RED}Red means the letter is not in the word
{colours.RESET}
Letters not used:
{' '.join(lettersNotUsed)}
    ''')


# Run the game
def runGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    global attempts, gameComplete, wordAttempts, start, lettersUsed, lettersNotUsed
    gameComplete = False
    attempts = 0
    wordAttempts = []
    lettersNotUsed = 'abcdefghijklmnopqrstuvwxyz'
    lettersNotUsed = list(lettersNotUsed)
    findWord()
    firstRun = True
    startScreen()
    wait = input('Press ENTER to start... \n')
    startScreen()
    start = time.time()
    print('Guess the word:')
    while gameComplete != True and attempts != 6:
        if firstRun == True:
            guessWord()
            checkWord()
            firstRun = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            startScreen()
            print('\n'.join(wordAttempts))
            guessWord()
            checkWord()
    if gameComplete == True:
        finalScore()
        startScreen()
        print('\n'.join(wordAttempts))
        print('Well Done, word successfully guessed!')
        print(f'You scored {score} points!')
        print(f'You took {timeTaken} seconds')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        startScreen()
        finalScore()
        print('\n'.join(wordAttempts))
        print(f"Unlucky, you didn't get it this time! \nThe word was: {word}")
        print(f'You took {timeTaken} seconds')


runGame()
