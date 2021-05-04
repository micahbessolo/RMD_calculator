# This is a tim travel text-based adventure game
# this is based off of the tutorial in https://www.youtube.com/watch?v=ypNFNr72Xe8&list=LL&index=12&t=139s
# 38:27
import sys
import time

a = 2
b = 0.2
c = 0.08

def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in thick vines.")
    time.sleep(a)
    print("You feel a round rock that sinks into the floor when you press it.")
    time.sleep(a)
    print("The ground starts rumbling.")
    time.sleep(a)
    print("Light begins flooding in .")
    time.sleep(a)
    print()
    s = '"I\'m in a cave..?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    print()
    print("The rock released a boulder that was blocking thecave entrance.")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Exit forward through the caves entrancce, into the light.")
    time.sleep(a)
    print("Path #2: Explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("Path #3: Climb down the vines into a bottomless hole in the ground.")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()

def path1():
    print()

def path1_1():
    print()

def path1_2():
    print()

def path2():
    print()

def path2_1():
    print()

def path2_2():
    print()

def path3():
    print("you climb down in vines into a bottomless hole in the ground ")
    time.sleep(a)
    print("It's dark, damp, and hard to climb down the vines, but your vision and muscles eventually adjust.")
    time.sleep(a)
    print("A huge boulders slides into place above you, blocking your escape.")
    time.sleep(a)
    print("You continue climbing down the vines until you hear something whirring up at you.")
    time.sleep(a)
    print("someone calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey, hey there!..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is HERMES... I'll be youre guide to freedom..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Yes, I know all about you! You're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the onw who trapped you in the time loop... "
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...I'm on my way to deliver a message, so I can't escort you personally..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, I can transport you there, or anywhere else on Mount OLYMPUS..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...CHORONOS is just below and he'll certainly TEST YOU when you meet him..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print()
    print("Hermes will transport you anywhere on Mount OLYMPUS:")
    time.sleep(a)
    print("Path #1: Continue below to face CHRONOS.:")
    time.sleep(a)
    print("Path #2: Read: THE SECRETS OF TIME.:")
    time.sleep(a)
    print("Path #3: Speak with ARES.")
    time.sleep(a)
    print("Path #4: Speak with ARTEMIS")
    time.sleep(a)
    print("Path #5: Speak with APOLLO.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2/3/4/5): ")
    if secondPath =='2':
        path2_2()
    elif secondPath == '3':
        path1_1()
    elif secondPath == '4':
        path1()
    elif secondPath == '5':
        path2()
    else:
        print()
    print("You continue down the vines until you reach the bottom.")
    time.sleep(a)
    print("You see a small old woman next to the largest red and black iron-wrought double doors you've ever seen.")
    time.sleep(a)
    print("The old woman calls out to you.")
    time.sleep(a)
    print()
    s8 = '"Hello there, young traveler...'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = '...My name is MOIRAE, I\'m in great need of help...'
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = '...I know who you seek... CHRONOS is just beyond this door...'
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s11 = '...If you enter, you may speak with him and restore your freedom.'
    for character in s11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s12 = '...But before you do so, would you take me HOME?...'
    for character in s12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s13 = '...I\'m unable to escape this cold, dark cave on my own...'
    for character in s13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s14 = '...The choice is yours."'
    for character in s14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print()
    print("Path #1 Forget the old woman. Enter the doors and speak with CHRONOS.")
    time.sleep(a)
    print("Oath #2: Honor the woman's request. Help MOIRAE return home safely.")
    time.sleep(a)
    thirdPath = input("Which path would you like to take? (1/2): ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()



def path3_1():
    print()
    print("You begin walking toward the doors, ignoring MOIRAE's request")
    time.sleep(a)
    print('"I would hel y9u out but I\'m in a bit of a hurry,m you understand."')
    time.sleep(a)
    print("You pull open the massive doors with all yof your might and enter.")
    time.sleep(a)
    print("Standing now in the largest room, in fornt of the largest man yo've ever seen.")
    time.sleep(a)
    print("The room is darkm but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s1 = '"ah... I\'ve been expecting you., But you\'re somewhat early...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...It appears you've taken a fairly hard route..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...And your strength has grown from your travels..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...However, there is still just one..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...One more thing you need to learn"
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...And learn you will..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...In time.\""
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    intro()

def path3_2():
    print("you begin walking toward MOIRAE, honoring her request.")
    time.sleep(a)
    print("I understand. I know what it\'s like to miss home... That\'s why I need to get out of here...'")
    time.sleep(a)
    print('But before I walk through those doors, I promise that I\'ll get you home safely."')
    time.sleep(a)
    print()
    print("You kneel in fornt of MOIRAE, allowing her to climb easily onto your back.")
    time.sleep(a)
    print("Standing up, you make your way back to the vine wall to make your ascent.")
    time.sleep(a)
    print("Just as you grab the vines, the enormous red and black iron doors thrust open, slamming to a halt.")
    time.sleep(a)
    print("The largest man you've ever seen steps out and his thunderous voice calls out to you.")
    time.sleep(a)
    print()
    s1 = '"ah...I\'ve been expecting your. And you\'re right on time!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s2 = '...It appears youy\'ve talem a very diffficult route...'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...And your strength has growth from your travels..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...You've even put others needs before your own..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...You have learned everything I have to teach you..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...So you may finally be free..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...It's time to return."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print()
    print("Thanks for playing!!!")



print()
print()
print("     #############################")
print("     #                           #")
print("     #        Time Unraveled     #")
print("     #############################")
print()
print()
time.sleep(a)
print("Wha... What happened? Where am I?")
time.sleep(a)
print("it's too dark to see anything...")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == 'n' or startGame == 'N':
    print("Maybe next time")
elif startGame == 'y' or startGame == 'Y':
    intro()
