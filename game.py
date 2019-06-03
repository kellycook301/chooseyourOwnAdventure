#! python 2
# name: Kelly Cook
# date: 5/14/19
# description: text-based adventure game

import sys; print(sys.version)
import time
import random

print ("")
print ("")
print ("O==============================================================================O")
print ("|                             ++ A Hero's Journey ++                           |")
print ("O==============================================================================O")
print ("")

# time.sleep(2)

def storyIntro():
    print("-STORY EXPOSITION GOES HERE -")
    levelOne()

# ALL OF THE PLAYAGAINS

def playAgain():
    answer = raw_input("play again? yes/no \n").lower().strip()
    if answer == "yes":
        print("")
        print("Let's try that again")
        print("")
        levelOne()

    elif answer == "no":
        print("")
        print("The world became shrouded in darkness")
        print("A millenia of unimaginable pain and suffering soon followed.")
        print("")
        

def playLevelTwoAgain():
    answer = raw_input("play again? yes/no \n").lower().strip()
    if answer == "yes":
        print("")
        print("Let's try that again")
        print("")
        levelTwo()

    elif answer == "no":
        print("")
        print("The world became shrouded in darkness")
        print("A millenia of unimaginable pain and suffering soon followed.")
        print("")

# ALL OF THE GAME ACTIONS

def confrontEnemy():
    print("")
    print("you confront enemy and win")
    print("")
    levelThree()

def leftResult():
    print("")
    print("Something where you went left")
    print("")

def rightResult():
    print("")
    print("Something where you went right")
    print("")

def backResult():
    print("")
    print("Something where you turned around")
    print("")

# ALL OF THE LEVELS

def levelOne():
    path = ""
    while path != "confront" and path != "escape":
        path = raw_input("confront/escape \n").lower().strip()

    if path == "confront":
        print("")
        print("Bad stuff happens")
        print("")
        print("GAME OVER")
        print("")
        playAgain()
    
    elif path == "escape":
        print("")
        print("You escape")
        print("")
        levelTwo()

def levelTwo():
        smash = ""
        while smash != "yes" and smash != "no":
            smash = raw_input("Confront new enemy? yes/no \n").lower().strip()
            if smash == "yes":
                print("")
                print("You hit that bitch")
                print("")
                confrontEnemy()

            if smash == "no":
                print("")
                print("You get murdered")
                print("")
                playLevelTwoAgain()

def levelThree():
        where = ""
        while where != "left" and where != "right" and where != "back":
            where = raw_input("Go right, left, or back? left/right/back \n").lower().strip()
            if where == "left":
                print("")
                print("You go left")
                print("")
                leftResult()

            if where == "right":
                print("")
                print("You go right")
                print("")
                rightResult()

            if where == "back":
                print("")
                print("You turn around")
                print("")
                backResult()

# START GAME BELOW

storyIntro()