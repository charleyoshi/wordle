import random
import sys
from rich import print


db = 'fiveLetterWords.txt'
wordList = []
answer = ''
isWin = False


def loadFile():
    global db
    global answer
    global wordList
    with open(db) as f:
        for line in f:
            wordList.append(line.strip())

    answer = random.choice(wordList).upper()
    

def play():
    print('------------------------------------------------------------------------')
    global isWin
    currentAttempt = 0
    maxAttempt = 5
    message = '_ _ _ _ _'
    
    while currentAttempt < maxAttempt:
        # play

        if currentAttempt == 0:
            print('\t{0} Let\'s guess! You have {1} attempts in total.'.format(message, maxAttempt - currentAttempt))

        else:
            print('{0} attempts left'.format(maxAttempt - currentAttempt))

        isValid = False
        while not isValid:
            userInput = input('Enter your guess: ').upper()
            if len(userInput) == len(answer) and userInput.isalpha() and userInput.lower() in wordList:
                isValid = True


        for i in range(len(userInput)):
            if userInput[i] == answer[i]:
                print('[reverse green] {} [reverse green]'.format(userInput[i]), end='')
            elif userInput[i] in answer:
                print('[reverse yellow] {} [reverse yellow]'.format(userInput[i]), end='')
            else:
                print('[reverse gray] {} [reverse gray]'.format(userInput[i]), end='')
        print('\n')

        if userInput == answer:
            isWin = True
            break

        currentAttempt += 1


def printResult():
    if isWin:
        # show Win message
        print('\tYou won! The answer is {0}'.format(answer))
    else:
        # show Lose message
        print('\tSorry! You lose. You\'ve ran out of attempts')
        print('\tThe answer is: {0}'.format(answer))



def main():
    try: 
        loadFile()
    except:
        print('OOOPS! No such file called \'{0}\' in your directory. Make sure you get the right name for your .txt file.'.format(db))
        sys.exit()
    play()
    printResult()



if __name__ == "__main__":
    main()