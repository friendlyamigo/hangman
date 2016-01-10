from sys import exit
from random import randint

class Hangman:
    def __init__(self, dict):
        self.dict = open(dict, 'r').readlines() # get dictionary
        self.guesses = 10 # guesses left
        self.correct = [] # correct letters
        self.incorrect = [] # incorrect letters
        self.ran_phrase = randint(0, len(self.dict)) - 1 #get random number for phrase
        self.phrase = self.dict[self.ran_phrase].strip()
        self.phrase_so_far = []

    def get_guess(self):
        self.guess = raw_input(">")
        # for an incorrect guess
        while (self.guess in self.correct or self.guess in self.incorrect) or (len(self.guess) !=1 or self.guess.isalpha() ==  False): #if answer is incorrect
            print "Try again"
            self.guess = raw_input(">")

        if self.guess in self.phrase:
            self.correct.append(self.guess)
        else:
            self.incorrect.append(self.guess)
            self.guesses -= 1

    def print_phrase_so_far(self):
        self.phrase_so_far = []
        for char in self.phrase:
            if char in self.correct or not char.isalpha():
                show = char + ' '
            else:
                show = '_ '
            self.phrase_so_far.append(show)
        print ''.join(self.phrase_so_far)

    def finished(self):
        if '_ ' not in self.phrase_so_far:
            print "You win!"
            exit()
        elif self.guesses == 0:
            print "You lose! The answer was: \"%s\"" % self.phrase
            exit()


player = Hangman("hangmandictionary.txt")

while True:
    print "You have %i guesses left!" % player.guesses
    print "Incorrect letters: %s" % player.incorrect
    player.get_guess()
    player.print_phrase_so_far()
    player.finished()
    print '\n'
