import random

attempt = 0

for i in range(1):
    random_number = (random.randint(1,10))

while attempt < 3:
    guess = input("Guess a number: ")
    if int(guess) < random_number:
        print("too small")
        attempt += 1
    elif int(guess) > random_number:
        print("too big")
        attempt += 1
    else:
        print("correct")
        break