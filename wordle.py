import random
from itertools import (takewhile,repeat)
from tkinter import TRUE
import os
import sys

wordfile ='wordlists/text.txt'
wordlist = open(wordfile, 'r')

class colours:
    RED = '\u001b[31m'
    AMBER = '\u001b[33m'
    GREEN = '\u001b[32m'
    RESET = '\u001b[0m'

def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\n') for buf in bufgen )
    f.close()

def findWord():
    global word, letters
    wordlistReadLines = wordlist.readlines()
    wordLine = random.randint(0, (rawincount(wordfile)-1))
    word = wordlistReadLines[wordLine]
    word = word.replace('\n', '')
    letters = list(word)


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
    attempts+=1
    

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
                    #print(f'{guess.index(x)} {x} {checkWord.index(y)} {y}')
                    if x == y:
                        if guess.index(x) == checkWord.index(y):
                            outcome.append(f'{colours.GREEN}{x}{colours.RESET}')
                            correctPlace = True
                            guess[guess.index(x)] = '!'
                            correct += 1
                        else:
                            if checkWord.count(y) > 1:
                                checkWord[checkWord.index(y)] = y+'!'
                            else:
                                outcome.append(f'{colours.AMBER}{x}{colours.RESET}')
                                correctLetter = True    
                                guess[guess.index(x)] = '!'
        else:
            outcome.append(f'{colours.RED}{x}{colours.RESET}')
    print(''.join(outcome))
    wordAttempts.append(''.join(outcome))

    if correct == 5:
        gameComplete = True
        print('Well Done, word successfully guessed!')
    else:
        print(f"Unlucky, you didn't get it this time! \n the word was: {word}")
    


def runGame():
    os.system('cls' if os.name=='nt' else 'clear')
    global attempts, gameComplete, wordAttempts
    gameComplete = False
    attempts = 0
    wordAttempts = []
    findWord()
    firstRun = True
    print(f'''
                       _ _      
__      _____  _ __ __| | | ___ 
\ \ /\ / / _ \| '__/ _` | |/ _ \\
 \ V  V / (_) | | | (_| | |  __/
  \_/\_/ \___/|_|  \__,_|_|\___|
                                
Welcome to Wordle clone by xhemals
You have 6 attempts to guess the word
{colours.GREEN}Green means you have the letter in the right space
{colours.AMBER}Amber means the letter is in the word
{colours.RED}Red means the letter is not in the word
{colours.RESET}
    ''')
    print('Guess the word:')
    while gameComplete != TRUE and attempts != 6:
        if firstRun == TRUE:
            guessWord()
            checkWord()

            #os.system('cls' if os.name=='nt' else 'clear') 
            firstRun = False
        else:
            os.system('cls' if os.name=='nt' else 'clear') 
            print(f'''
                       _ _      
__      _____  _ __ __| | | ___ 
\ \ /\ / / _ \| '__/ _` | |/ _ \\
 \ V  V / (_) | | | (_| | |  __/
  \_/\_/ \___/|_|  \__,_|_|\___|
                                
Welcome to Wordle clone by xhemals
You have 6 attempts to guess the word
{colours.GREEN}Green means you have the letter in the right space
{colours.AMBER}Amber means the letter is in the word
{colours.RED}Red means the letter is not in the word
{colours.RESET}
            ''')
            print('\n'.join(wordAttempts))
            guessWord()
            checkWord()

            #os.system('cls' if os.name=='nt' else 'clear') 


runGame()