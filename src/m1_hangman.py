"""
Hangman.

Authors: Triston Hine.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
import random
def randword():
    open('words.txt').readline()
    string = open('words.txt').read()
    words = string.split()
    r = random.randrange(0, len(words))
    item = words[r]
    return item

def guess():
    string = input('Please enter a letter: ')
    return string

def compare(word, character):
    y = []
    for k in range(len(word)):
        if word[k] == character:
            y = y + [k]
    return y

def main():
    x = randword()
    print(x)
    closeness = []
    turns = 0
    closeness = []
    for u in range(len(x)):
        closeness = closeness + ['-']
    while turns < 7:
        wordsin = guess()
        y = compare(x, wordsin)
        if len(y) == 0:
            turns = turns + 1
        for k in range(len(x)):
            for r in range(len(y)):
                if(y[r] == k):
                    closeness[k] = x[k]
        for p in range(len(closeness)):
            print(closeness[p], end='')
        print('')
        e = ''
        for o in range(len(closeness)):
            e = e + closeness[o]
        if e == x:
            print("Looks like you win this round, go again?")
            string = input('yes or no: ')
            if string == 'yes':
                main()
            else:
                return 'Very well then'




main()