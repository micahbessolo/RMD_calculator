word = "nutted"

lGuessLimit = 3
wGuessLimit = 3

while lGuessLimit > 0:
    letterGuess = input("Guess a letter: ")
    _word = word
    for item in word:
        if item != letterGuess:
            _word = _word.replace(item, '_')
    lGuessLimit -= 1
    print(_word)

