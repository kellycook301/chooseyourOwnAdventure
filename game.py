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

print("                                   ($$$$$$$$$)")
print("                                    ($$$$$$$)")
print("                                  (1$$$$$$$$$$$)")
print("                                     ($$$$$)")
print("               ($)                   ($$$$$)               ($)")
print("              ($$)                   ($$$$$)                ($$)")
print("             ($$)                    ($$$$$)                 ($$)")
print("            ($$)                     ($$$$$)                  ($$)")
print("            ($$$)                    ($$$$$)                  ($$$)")
print("             ($$$$)                  ($$$$$)                 ($$$$)")
print("              ($$$$$)                ($$$$$)                ($$$$$)")
print("               ($$$$$)               ($$$$$)               ($$$$$)")
print("                ($$$$$)            ($$$$$$$$$)            ($$$$$)")
print("                  ($$$$$$$)      ($$$$$$$$$$$$$)      ($$$$$$$)")
print("                ($$$$$$$$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$$$$$$$$)")
print("                      ($$$$$$$$$$$$$$$$___$$$$$$$$$$$$$$$$)")
print("                 ($$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$)")
print("                                ($$$$$$$$$$$$$$$$$)")
print("                                    ($$$$$$$)")
print("                                  ($$$$$$$$$$$)")
print("                                 ($$$_______$$$)")
print("                                  ($$$_____$$$)")
print("                               ($____$$$_$$$____$)")
print("                                ($$$$$$$^$$$$$$$)")
print("                                   ($$$$^$$$$)")
print("                                    ($$$^$$$)")
print("                                 ($__$$$^$$$__$)")
print("                                  ($$$$$^$$$$$)")
print("                                   ($$$$^$$$$)")
print("                              ($____($$$^$$$)____$)")
print("                              ($$____$$$^$$$____$$)")
print("                               ($$$$$$$$^$$$$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                    ($$$^$$$)")
print("                                   ($$$$^$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                 ($$$$$$^$$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                  ($$$$$^$$$$$)")
print("                                   ($$$$^$$$$)")
print("                                   ($$$$^$$$$)")
print("                                   ($$$$^$$$$)")
print("                                   ($$$$^$$$$)")
print("                                   ($$$$^$$$$)")
print("                                    ($$$^$$$)")
print("                                    ($$$^$$$)")
print("                                    ($$$^$$$)")
print("                                     ($$^$$)")
print("                                     ($$^$$)")
print("                                     ($$^$$)")
print("                                      ($^$)")
print("                                      ($^$)")
print("                                      ($$$)")
print("                                       ($)")
print("")
print("")

# time.sleep(2)

def displayIntro():
    print("Mountain raiders are outside your door.")

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

def levelOne():
    path = ""
    print("-STORY EXPOSITION GOES HERE -")
    while path != "confront" and path != "escape":
        path = raw_input("Do you open the door and confront your father's killers?. Or do you escape through the window? confront/escape \n").lower().strip()

    if path == "confront":
        print("")
        print("You swing open the door to confront your father's killers.")
        print("Behind it are three men in imperial armor.")
        print("'The king's men? But wh-'")
        # time.sleep(3)
        print("Before you can finish your thought you feel the cold sting of a silvery blade quickly enter and leave your chest.")
        # time.sleep(3)
        print("You slump to the ground and take your last breath. A tall, bearded figure in royal armor and garb steps before your lifeless body.")
        # time.sleep(3)
        print("He kicks you just to make sure and then sheathes his blade, making sure to wipe it beforehand.")
        # time.sleep(3)
        print("'Dispose of the boy and clean up this mess. Report to His Majesty and alert him that it has been taken care of.'")
        # time.sleep(3)
        print("")
        print("GAME OVER")
        # time.sleep(3)
        print("")
        playAgain()
    
    elif path == "escape":
        print("")
        print("'It would be far too risky to confront the guys outside my door'.")
        print("'They're probably armed too and I don't have a sword.'")
        print("You slowly open the window. It let's out a soft *creeeeeeak* as you do.")
        # time.sleep(3)
        print("Your heart is racing.")
        # time.sleep(3)
        print("You're on the second floor, but the drop shouldn't be too bad.")
        print("Time's running out. Just as you get your second leg out the window your door swings wide open.")
        # time.sleep(3)
        print("'HEY! DON'T LET HIM ESCAPE!' It's a knight in royal armor and he's headed right towards you.")
        # time.sleep(3)
        print("'What the hell are the kings men doing here?', you wonder.")
        # time.sleep(3)
        print("But there's no time. You leap out of the window into the bushes below.")
        # time.sleep(3)
        print("*CRACK*")
        # time.sleep(2)
        print("You take a hard fall and break your ankle. But you need to get moving. You hobble your way to the woods at the edge of the farm.")
        # time.sleep(3)
        print("The knight pops his head out of the window. 'Shit! He's getting away!")
        # time.sleep(2)
        print("The moon gives you just enough light to safely make it into the forest. You take shelter behind a large boulder.")
        print("A lone knight enters the forest looking for you. Not noticing you, he slowly passes by. By you is a rather large rock that you could use to knock him out and take his sword. ")

def levelTwo():
        smash = ""
        while smash != "yes" and smash != "no":
            smash = raw_input("Do you take the rock and try and smash it over his head? yes/no \n").lower().strip()
            if smash == "yes":
                print("")
                print("You hit that bitch.")
                print("")
                (takeSword)

            if smash == "no":
                print("")
                print("He wrestles with you and stabs you in the dick and you die and it sucks.")
                print("")
                playLevelTwoAgain()


# Start game below

levelOne()
levelTwo()