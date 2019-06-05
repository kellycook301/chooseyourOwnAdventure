#! python 2
# name: Kelly Cook
# date: 5/14/19
# description: text-based adventure game

import sys; print(sys.version)
import time
import random


print ("")
print ("O==============================================================================O")
print ("|                             ++ A Hero's Journey ++                           |")
print ("O==============================================================================O")
print ("")

# time.sleep(2)

def storyIntro():
    # create input for character age, etc.
    character_Name = raw_input("What would you like your character's name to be?: ")
    print("")
    print("Hello, " + character_Name + "!")
    confrontOrEscape(character_Name)

### ALL OF THE PLAYAGAINS ###

def playAgain():
    answer = ""
    while answer != "yes" and answer != "no":
        print("Would you like to play again?")
        answer = raw_input("yes/no \n").lower().strip()
        
    if answer == "yes":
        print("")
        print("Let's try that again")
        print("")
        print "\033c"
        confrontOrEscape()

    elif answer == "no":
        print("")
        print("The world became shrouded in darkness")
        print("A millenia of unimaginable pain and suffering soon followed.")
        print("")
        
### ALL OF THE GAME ACTIONS ###

def confrontOrEscape(name):
    path = ""
    while path != "confront" and path != "escape":
        print("The bandits are coming up the stairs, " + name + ". You're going to have to fight them or make a break through the window.")
        path = raw_input("Do you attempt to confront the enemy or escape? confront/escape \n").lower().strip()

    if path == "confront":
        print("")
        print("You go and confront the enemy.")
        print("More story exposition.")
        print("He asks if you would like to join him and his leader in conquest.")
        print("")
        joinOrEscape()
    
    elif path == "escape":
        print("")
        print("You escape")
        print("")

def goHomeOrFollow():
    home = ""
    while home != "go home" and home != "follow":
        home = raw_input("Do you turn and go back home or follow the enemy? go home/follow \n").lower().strip()

    if home == "go home":
        print("")
        print("You decide that it is best to leave the group be and not seek revenge.")
        print("You make your way back to your home and go inside.")
        print("In the kitchen is the corpse of your father who was slain by the nomad horde.")
        print("")
        buryOrDie()
        print("")

    elif home == "follow":
        print("")
        print("You decide to follow the group through the forest.")
        print("You track then until nightfall.")
        print("Once they have fallen asleep in their tents you strike.")
        print("")
        confrontOrSubmit()
        print("")

def confrontOrSubmit():
    confront = ""
    while confront != "confront" and confront != "wake them":
        confront = raw_input("Do you confront the enemy by attacking their leader in his sleep or by waking them up to talk to them? confront/wake them \n").lower().strip()

    if confront == "confront":
        print("")
        print("You go to the bigger tent in the group and take a sword that is placed by the doorway.")
        print("You raise the sword above your head in preparation to strike.")
        print("You drive it through the blankets but do not feel a body underneath.")
        print("It was a pile of pillows disguised as a body.")
        print("SHING")
        print("You feel the cold steel of a blade pierce your abdomen.")
        print("'Don't think I'm so foolish. I heard you from a mile away.'")
        print("The leader of the horde then kicks your struggling body to the ground and takes off your head in one fell swoop.")
        print("'Pathetic'")
        print("")
        playAgain()
        print("")

    elif confront == "wake them":
        print("")
        print("You grab a sleeping soldier who looked as though he was to be on guard duty and plunge his own sword into his own stomach.")
        print("The man crumbles and falls to the ground. His armour making quite a ruckus.")
        print("You yell for the leader to show his face.")
        print("Every soldier scrambles getting up and out of their tents; drawing their swords ready to pounce on you and tear you limb from limb")
        print("A tall man appears from the largest tent.")
        print("'And who might you be?'")
        print(storyIntro.character_Name + "you say.")
        print("You explain that you are the son of a farmer and that they have killed your father in cold blood.")
        print("'AH. The boy who escaped earlier. I remember. I remember.'")
        print("'You know...it takes a lot of courage to come here in the middle of the night and confront all of us.'")
        print("'You even seemed to have taken care of a useless guard who was meant to be keeping watch. What say you join us?'")
        print("'Here you will do many great things. See many riches. Enjoy the company of many women. And you can eat till your belly is full.'")
        print("'Surely not something you experienced as a poor farm boy.'")
        print("")
        killOrSwearAllegiance()
        print("")

def killOrSwearAllegiance():
    swear = ""
    while swear != "swear allegiance" and swear != "kill him":
        swear = raw_input("Do you swear allegiance to him and live a lavish life or kill him for murdering your father? swear allegiance/kill him \n").lower().strip()

    if swear == "swear allegiance":
        print("")
        print("You realize that risking your life over a revenge plot is not the way you want to go out.")
        print("You tell him to swear that he is not lying.")
        print("'I promise. All of this can be yours. The riches, the women, the food...all yours if you join.")
        print("The soldiers all murmur.")
        print("'He can't be serious can he?'")
        print("'He killed Johnny too.'")
        print("'Well, he did fall asleep on guard duty.'")
        print("'It's his fault really.'")
        print("You drop the sword and agree to join his group of bandits.")
        print("Many years later you command a legion of men who wander the continent pillaging and murdering.")
        print("Darkness spreads across the land for millenia under your rule.")
        print("")
        playAgain()
        print("")

    elif swear == "kill him":
        print("")
        print("You bring the sword up and scream as you run towards the bandit leader.")
        print("Before you can take ten steps an arrow pierces your heart and you fall to the ground, dying instantly.")
        print("'Fool. You could have had it all.'")
        print("Your body is picked up and tossed into the fire.")
        print("")
        playAgain()
        print("")

def buryOrDie():
    bury = ""
    while bury != "bury dad" and bury != "take knife":
        bury = raw_input("Do you bury your father or take the knife and end your suffering? bury dad/take knife \n").lower().strip()

    if bury == "bury dad":
        print("")
        print("You go outside to the family lot and start digging a hole for your father.")
        print("Tears begin to swell up.")
        print("At the edge of the forest two men from before notice you and make their way back towards your house.")
        print("")
        playAgain()
        print("")

    elif bury == "take knife":
        print("")
        print("You take a knife from the kitchen table and plunge it into your chest.")
        print("You fall next to your father's corpse and slowly fade away.")
        print("")
        playAgain()
        print("")

def joinOrEscape():
    join = ""
    while join != "join" and join != "escape":
        join = raw_input("Join the enemy or escape? join/escape \n").lower().strip()

    if join == "join":
        print("")
        print("You join the enemy.")
        print("")
        continueOrMeet()
        print("")

    elif join == "escape":
        print("")
        print("You run into the forest far away from the enemy.")
        print("You find a cave for shelter and hide there for a few days untill things die down.")
        print("After five days you emerge from the cave.")
        print("While walking through the forest you see the crew from earlier off in the distance.")
        print("")
        goHomeOrFollow()
        print("")

def continueOrMeet():
    meet = ""
    while meet != "continue" and meet != "meet":
        meet = raw_input("Join him in continuing his campaign immediately or go and meet the leader; the man who killed your father? continue/meet \n").lower().strip()
        
    if meet == "continue":
        print("")
        print("You decide to meet the leader at another time.")
        print("You join his campaign to see where it will take you. Maybe you can get some intel.")
        print("Maybe you can get some intel.")
        print("Your caravan is being attacked by rebels.")
        print("You have the enemy in your sights.")
        print("")
        lowerOrShoot()
        print("")
                
    elif meet == "meet":
        print("")
        print("You decide to go meet the leader; the man who ordered the death of your father and countless others.")
        print("Story exposition")
        print("")
        killOrSwearAllegiance()
        print("")

def lowerOrShoot():
    shoot = ""
    while shoot != "lower" and shoot != "shoot":
        shoot = raw_input("Lower your weapon or shoot the enemy? lower/shoot \n").lower().strip()
        
    if shoot == "lower":
        print("")
        print("You lower your weapon and are spotted.")
        print("The enemy takes a shot at you and the arrow pierces your heart.")
        print("")
        print("GAME OVER")
        print("")
        playAgain()
        print("")

    elif shoot == "shoot":
        print("")
        print("The enemy is wounded on the battlefield and cannot fight back")
        print("")
        killOrSpare()
        print("")

def killOrSpare():
    kill = ""
    while kill != "kill" and kill != "spare":
        kill = raw_input("Do you kill the rebel who attempted to murder you or do you spare her life? kill/spare \n").lower().strip()
    
    if kill == "kill":
        print("")
        print("You sink your sword into the rebel's chest.")
        print("After a minute of squirming, you end her suffering by decapitation.")
        print("The captain puts his hand on your shoulder.")
        print("'Your ruthlessness will make you a fine captain someday.'")
        print("You look down at the corpse and wonder what kind of monster you will become.")
        print("Many years later you command a legion of men who wander the continent pillaging and murdering.")
        print("Darkness spreads across the land for millenia under your rule.")
        print("")
        playAgain()
        print("")

    elif kill == "spare":
        print("")
        print("You sheathe your sword and walk away.")
        print("The captain screams,")
        print("'What the hell are you doing?!'")
        print("'Cuff him!'")
        print("The captain and his men cuff you. You have been demoted to a slave amongst his crew.")
        print("Many decades go by and you become old and frail.")
        print("The captain's son who has been leading the crew since his father's death sees no need for you anymore.")
        print("He orders you to be killed.")
        print("You are left by the side of the road, forgotten by all, missed by none.")
        print("")
        playAgain()
        print("")

### START GAME BELOW ###
### This basically starts everything. Everything is tied to this one function ###


storyIntro()