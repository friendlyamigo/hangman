from sys import exit #exit command
from random import randint #to get random phrase

txtFile = open("hangmandictionary.txt") #open hangmandictionary.txt
phraseList = txtFile.read().split("\n") #make dictionary list
guessamount = 10 #guesses left
correct = [] #correct letters
incorrect = [] #incorrect letters
guesslist = [] #the list of underscrores and letters
ranPhrase = randint(0, len(phraseList) - 1) #get random number
phrase = phraseList[ranPhrase] #choose random word from phrase list

while guessamount > 0: #main loop

    print '\n' #new line
    print "Incorrect answers: ", incorrect #incorrect letter list
    guess = raw_input(">") #user input

    while (guess in correct or guess in incorrect) or (len(guess) !=1 or guess.isalpha() ==  False): #if answer is incorrect
        print "Try again"
        guess = raw_input(">")

    if guess in phrase: #test if guess is correct
        correct.append(guess)
        guessamount += 1

    else: #if guess is wrong
        incorrect.append(guess)

    for char in phrase: #print the phrase so far
        if char in correct or char.isalpha() == False: #if letter has been typed
            show = char + ' '
        else: #if letter has not been typed
            show = '_ '
        guesslist.append(show)

    print ''.join(guesslist) #print phrase so far

    if '_ ' not in guesslist:
        print "done"
        exit()

    guesslist = [] # reset list
    guessamount -= 1 # subtract guesses
    print guessamount, "guesses left"

else:
    print "You lose"
    print "the answer was: ", phrase
    exit()
