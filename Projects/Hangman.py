word = "nutted"
letterCount = len(word)
lGuessLimit = 6
wGuessLimit = 3

print(fr"This is a {letterCount} letter word")

while lGuessLimit > 0:
    letterGuess = input("Guess a letter: ")
    _word = word
    for item in word:
        if item != letterGuess:
            _word = _word.replace(item, '_')
    lGuessLimit -= 1
    print(_word)

while wGuessLimit > 0:
    wordGuess = input("Guess a word: ")
    if wordGuess != word:
        print("no.")
        wGuessLimit -= 1
    elif wordGuess == word:
        print("You win!!")
        break
