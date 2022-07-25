import os
import sys
import urllib.request
import json

import random
# colours for terminal


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


os.system('clear')

with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
    #   get the word data from the request
    data = json.loads(url.read().decode())
    word = data['data']


word = data['data'][random.randint(0, 2500)]

display = []
lives = 10
i = 0
guesses = []
while i < len(word):
    display.append('_')
    i += 1
print(display)

while "_" in display:
    if lives != 0:
        guess = input("guess a letter: ")
        guess = guess.lower()
        # invalid input
        if guess == "" or len(guess) > 1 or not guess.isalpha():
            print('please enter a single valid letter')
            continue
        if guess in guesses:
            print('you\'ve already guessed that letter... Try again.')
            continue
        # if guess is in the word
        if guess in word:
            # loop through word, find all instances
            # and replace _ with the correct letter
            i = 0
            while i < len(word):

                if guess == word[i]:
                    display[i] = guess
                i = i + 1

            print(bcolors.OKGREEN + 'Correct: ' + str(display) + bcolors.ENDC)
        # letter not in the word
        else:
            lives = lives - 1
            print(bcolors.WARNING + 'Nope. You now have ' +
                  str(lives) + ' lives left' + bcolors.ENDC)
        guesses.append(guess)
        print('letters used: ' + str(guesses))
    else:
        # failed
        print('You have ran out of lives. The word was: ' + word)
        sys.exit()

# won
print('Yay, you won the game. the word was: ' + word + '\n\n')
exit
