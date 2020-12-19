#! python 2
# name: Kelly Cook
# date: 5/14/19
# description: text-based adventure game

# variables can be passed into other methods as arguments and then be called.
# if the character_Name is to be used, just make sure that it follows down the list of
# methods so it remains in scope.
# probably not the best way for it to be done, but it makes sense to me.

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
    print("Let's get started.")
    print("")
    print("-- LOTS OF STORY EXPOSITION --")
    print("")
    confrontOrEscape(character_Name)

### ALL OF THE PLAYAGAINS ###

def playAgain(name):
    answer = ""
    while answer != "yes" and answer != "no":
        print("Would you like to play again?")
        answer = raw_input("yes/no \n").lower().strip()
        
    if answer == "yes":
        print("")
        print("Let's try that again")
        print("")
        print "\033c"
        confrontOrEscape(name)

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
        path = raw_input("Do you attempt to confront the enemy or escape?? confront/escape \n").lower().strip()

    if path == "confront":
        print("")
        print("You go and confront the enemy.")
        print("More story exposition.")
        print("He asks if you would like to join him and his leader in conquest.")
        print("")
        joinOrEscape(name)
    
    elif path == "escape":
        print("")
        print("You escape to the woods.")
        print("You take shelter at the mouth of a cave.")
        print("You can hear a bandit make his way towards you.")
        print("You can take shelter by going further into the cave or you can see if you can take out the lone bandit.")
        print("")
        escapeToTheWoods(name)
        print("")

### LEFT HAND SIDE CHOICES ###        

def joinOrEscape(name):
    join = ""
    while join != "join" and join != "escape":
        join = raw_input("Join the enemy or escape? join/escape \n").lower().strip()

    if join == "join":
        print("")
        print("You join the enemy, " + name + ".")
        print("")
        continueOrMeet(name)
        print("")

    elif join == "escape":
        print("")
        print("You run into the forest far away from the enemy.")
        print("You find a cave for shelter and hide there for a few days untill things die down.")
        print("After five days you emerge from the cave.")
        print("While walking through the forest you see the crew from earlier off in the distance.")
        print("")
        goHomeOrFollow(name)
        print("")

def continueOrMeet(name):
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
        lowerOrShoot(name)
        print("")
                
    elif meet == "meet":
        print("")
        print("You decide to go meet the leader; the man who ordered the death of your father and countless others.")
        print("Story exposition")
        print("")
        killOrSwearAllegiance(name)
        print("")

def lowerOrShoot(name):
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
        playAgain(name)
        print("")

    elif shoot == "shoot":
        print("")
        print("The enemy is wounded on the battlefield and cannot fight back")
        print("")
        killOrSpare(name)
        print("")   

def killOrSwearAllegiance(name):
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
        playAgain(name)
        print("")

    elif swear == "kill him":
        print("")
        print("You bring the sword up and scream as you run towards the bandit leader.")
        print("Before you can take ten steps an arrow pierces your heart and you fall to the ground, dying instantly.")
        print("'Fool. You could have had it all.'")
        print("Your body is picked up and tossed into the fire.")
        print("")
        playAgain(name)
        print("")    

def killOrSpare(name):
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
        playAgain(name)
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
        playAgain(name)
        print("")         

def goHomeOrFollow(name):
    home = ""
    while home != "go home" and home != "follow":
        home = raw_input("Do you turn and go back home or follow the enemy? go home/follow \n").lower().strip()

    if home == "go home":
        print("")
        print("You decide that it is best to leave the group be and not seek revenge.")
        print("You make your way back to your home and go inside.")
        print("In the kitchen is the corpse of your father who was slain by the nomad horde.")
        print("")
        buryOrDie(name)
        print("")

    elif home == "follow":
        print("")
        print("You decide to follow the group through the forest.")
        print("You track then until nightfall.")
        print("Once they have fallen asleep in their tents you strike.")
        print("")
        confrontOrSubmit(name)
        print("")

def buryOrDie(name):
    bury = ""
    while bury != "bury dad" and bury != "take knife":
        bury = raw_input("Do you bury your father or take the knife and end your suffering? bury dad/take knife \n").lower().strip()

    if bury == "bury dad":
        print("")
        print("You go outside to the family lot and start digging a hole for your father.")
        print("Tears begin to swell up.")
        print("At the edge of the forest two men from before notice you and make their way back towards your house.")
        print("")
        playAgain(name)
        print("")

    elif bury == "take knife":
        print("")
        print("You take a knife from the kitchen table and plunge it into your chest.")
        print("You fall next to your father's corpse and slowly fade away.")
        print("")
        playAgain(name)
        print("")


def confrontOrSubmit(name):
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
        playAgain(name)
        print("")

    elif confront == "wake them":
        print("")
        print("You grab a sleeping soldier who looked as though he was to be on guard duty and plunge his own sword into his own stomach.")
        print("The man crumbles and falls to the ground. His armour making quite a ruckus.")
        print("You yell for the leader to show his face.")
        print("Every soldier scrambles getting up and out of their tents; drawing their swords ready to pounce on you and tear you limb from limb")
        print("A tall man appears from the largest tent.")
        print("'And who might you be?'")
        print("'It's " + name + ".'")
        print("You explain that you are the son of a farmer and that they have killed your father in cold blood.")
        print("'AH. The boy who escaped earlier. I remember. I remember.'")
        print("'You know...it takes a lot of courage to come here in the middle of the night and confront all of us.'")
        print("'You even seemed to have taken care of a useless guard who was meant to be keeping watch. What say you join us?'")
        print("'Here you will do many great things. See many riches. Enjoy the company of many women. And you can eat till your belly is full.'")
        print("'Surely not something you experienced as a poor farm boy.'")
        print("")
        killOrSwearAllegiance(name)
        print("")

### RIGHT HAND SIDE CHOICES ###

def escapeToTheWoods(name):
    run = ""
    while run != "hide" and run != "attack":
        run = raw_input("Do you go further into the cave or try and take out the bandit by sneaking up and hitting him with a rock? hide/attack \n").lower().strip()

    if run == "hide":
        print("")
        print("You make your way further into the cave to avoid detection by the bandits or any of his comrades.")
        print("You move further back into the cave.")
        print("You hear a noise and take shelter behind a rock to avoid any detection.")
        print("A bandit makes his way towards the cave.")
        print("He takes a quick glance in.")
        print("'Huh. Thought I heard something.'")
        print("The bandit then turns around and walks away.")
        print("You take a second just to make sure he's gone and then plan your next move.")
        print("You decide to make your way further into the cave.")
        print("You come to a fork and see that you can either go left or right.")
        print("here is a smaller hole on the right, but there seems to be some kind of visible dim light coming through.")
        print("The hole on the left is much darker and doesn't seem to have any light coming from it.")
        print("It also appears to go deeper down into the cave.")
        leftRight(name)
        print("")

    if run == "attack":
        print("")
        print("You pick up a sizable rock and start sneaking towards the bandit, being careful not too make too much noise")
        print("and waiting until he's got his back to you.")
        shoutOrSilent(name)
        print("")

def shoutOrSilent(name):
    shout = ""
    while shout != "shout" and shout != "silent":
        shout = raw_input("He's in your sights. Do you attack silently or by screaming, hoping to throw him off guard? silent/shout \n").lower().strip()

    if shout == "shout":
        print("")
        print("You get at a good distance and run towards him, screaming at the top of your lungs.")
        print("The bandit is totally startled and goes for his short sword, but fumbles it out of fear.")
        print("You smash the rock over his head. The bandit stumbles and falls backwards over a 30-foot cliff.")
        print("You then make your way back to the cave to plan your next move.")
        print("")
        print("As you climb further and further down a thick green fog begins to form")
        print("'Wow. I didn't think I was in the fucking JUNGLE. Wheere did this fog come from?' you wonder.")
        print("You go through the fog and notice that there is a fork ahead of you.")
        print("...like a divulging path. Not a literal fork...you get it.")
        print("'Ah shit. One of these, huh?'")
        print("")
        leftRight(name)
        print("")

    if shout == "silent":
        print("")
        print("You start sneaking up behind the bandit and get within a good distance.")
        print("You raise the rock over your head and prepare to smash his brains in.")
        print("In an instant the bandit side-steps and takes a swipe at your mid-section with his short sword.")
        print("You drop and the rock on your foot and fall to the ground.")
        print("You bleed out and die a painful death.")
        print("")
        playAgain(name)
        print("")        

def leftRight(name):
    direction = ""
    while direction != "left" and direction != "right":
        direction = raw_input("Do you take the left path or the right path? left/right \n").lower().strip()

    if direction == "left":
        print("") 
        print("You decide to go down the bigger cavern to the left. It's dark but at least you won't be insanely claustrophobic.")
        print("You keep trekking down until you reach ther end of the tunnel. At then end is a large door about ten feet tall with torches on each side.")
        turnBackOrGoIn(name)
        print("")

    if direction == "right":
        print("") 
        print("A smaller cave is no problem to you. You decide to climb into the smaller hold head first.")
        print("You inch forward every so slowly. It feels like forever, but you reach the source of the dim light.")
        print("You crawl out of the hole and emerge into a large cave with a single bright torch.")
        print("Beside the torch is a tall figure in a black cape that covers its entire body.")
        print("Its decaying hand outstrecthes to yours.")
        print(name + ", I seeeeee rightttt throuuuuugh yooooou. Yooooou havvvvve commmmmeeee herrrrre lookinnnnnnng forrrr answersssss.'")
        print("'I haaaaave whatttttt yoooooou seeeeeeek.'")
        print("Before you appears two swords.")
        print("'Withhhhhhh thissssss youuuuu cannnnnnn takeeeeee baccccck whatttttt isssss yoursssss. Yourrrrrr faaaaaaaather.'")
        youWentRight(name)
        print("")

def turnBackOrGoIn(name):
    door = ""
    while door != "go in" and door != "turn back":
        door = raw_input("Do you go through the door or turn back and go the other way? go in/turn back \n").lower().strip()

    if door == "go in":
        print("")
        print("You enter the door and there is a crazy old witch lady.")
        print("She has a riddle for you. If you can answer it correctly she will give you a sword to vanquish your foes with ease.")
        print("If you fail, you will die.")
        witchRiddle(name)
        print("")

    if door == "turn back":
        print("")
        print("You decide to turn around and not see what craziness awaits you on the other side of the door")
        print("You make your way back up the fork in the cave and go down the right side instead.")
        print("A smaller cave is no problem to you. Could be better than the creepy door. You decide to climb into the smaller hold head first.")
        print("You inch forward every so slowly. It feels like forever, but you reach the source of the dim light.")
        print("You crawl out of the hole and emerge into a large cave with a single bright torch.")
        print("Beside the torch is a tall figure in a black cape that covers its entire body.")
        print("Its decaying hand outstrecthes to yours.")
        print(name + ", I seeeeee rightttt throuuuuugh yooooou. Yooooou havvvvve commmmmeeee herrrrre lookinnnnnnng forrrr answersssss.'")
        print("'I haaaaave whatttttt yoooooou seeeeeeek.'")
        print("Before you appears two swords.")
        print("'Withhhhhhh thissssss youuuuu cannnnnnn takeeeeee baccccck whatttttt isssss yoursssss. Yourrrrrr faaaaaaaather.'")
        youWentRight(name)
        print("")

def youWentRight(name):
    sword = ""
    while sword != "left" and sword != "right":
        sword = raw_input("Do you take the crimson sword on the left or the pitch black one on the right? left/right \n").lower().strip()

    if sword == "left":
        print("")
        print("You pick the crimson sword.")
        print("'Many mennnnn havvvvvve mettttt theeeeeir endddddd byyyyyy thissssss sworrrrrrrd. A Great Sacrifice isssssss requirrrrrrred. Goodddddddd lucccccccck.'")
        print("The creature disappears and you are surrounded by a blinding light.")
        print("You find yourself in a lush field near your house.")
        print("You turn around to thank the creature but the cave is gone. You can only see the forest that is a few hundred yards out.")
        print("You head in the direction of where the bandits were going.")
        print("You reach their camp by nightfall and take shelter up in a tree further away from where they've stationed themselves.")
        midnightStrike2(name)
        print("")
    
    if sword == "right":
        print("")
        print("You pick the pitch black sword.")
        print("'Inttttttteressssting. I nowwwww sssseeeeee yourrrrr Heart. Goooodddddddd lucccccccck.'")
        print("The creature disappears and you are surrounded by a blinding light.")
        print("You find yourself in a lush field near your house.")
        print("You turn around to thank the creature but the cave is gone. You can only see the forest that is a few hundred yards out.")
        print("You head in the direction of where the bandits were going.")
        print("You reach their camp by nightfall and take shelter up in a tree further away from where they've stationed themselves.")
        print("At midnight the pitch black sword begins to glow a deep purple.")
        print("The sword speaks...")
        print("'TRAVELER...I SEE YOUR HEART. I SEE YOUR GREATEST WISH. I SEE A GREAT DISTURBANCE. A WORLD OF VIOLENCE.'")
        print("'NOW, I WILL TAKE WHAT IS MINE.'")
        print("The sword fuses with your arm and you scream in agony.")
        print("'A TIME OF GREAT CLEANSING IS UPON US.'")
        print("Many purple lights shoot forth from the sword and head towards the camp. The screams of soldiers are heard.")
        print("You run towards the camp to find the soldiers engulfed in dark flames.")
        print("You make your way towards the larger tent where the leader is stationed and enter it.")
        print("'YOU. WHAT DID YOU DO? Demon, have you come for me as well?'")
        print("Your arm feels as though it is on fire. You notice a sword in the hands of a felled soldier.")
        midnightStrike3(name)
        print("")


def midnightStrike2(name):
    strike2 = ""
    while strike2 != "cut it off" and strike2 != "kill him":
        strike2 = raw_input("Do you cut off your arm to stop the pain or kill the leader now? \n cut it off/kill him").lower().strip()

    if strike2 == "cut it off":
        print("")
        print("You reach for the sword in the hands of the felled soldier and cut off your cursed arm.")
        print("The sword breaks into a hundred pieces. You could not break the skin.")
        print("'TRY TO KILL ME, WILL YOU?'")
        print("Your fused arm pulsates and it hurts like hell. A black tentacle emerges from the center of your chest and pierces Solomon, cutting him in two.")
        print("")


def witchRiddle(name):
    answer = ""
    while answer != "red" and answer != "white" and answer != "blue" and answer != "all three":
        answer = raw_input("What are the colors of the American flag? red/white/blue/all three \n").lower().strip()

    if answer == "red":
        print("")
        print("'HAHAHAHA NOT.'")
        print("The witch casts a fire spell and you burst into flames.")
        print("The witch produces a single shrimp and attaches it to a long stick. She holds it out and uses your burning body to cook the shrimp.")
        playAgain(name)
        print("")

    if answer == "white":
        print("")
        print("'WRONG.'")
        print("The witch picks up a trident and throws it right into your chest. You bleed out and die the most painful death.")
        print("Foolish boy.")
        playAgain(name)
        print("")

    if answer == "blue":
        print("")
        print("'PFFFFT AS IF.'")
        print("The witch draws a sword and cleaves off your head. She holds it in front of your body as it collapses.")
        print("The last thing you heard is the witch's intense cackling.")
        playAgain(name)
        print("")

    if answer == "all three":
        print("")
        print("'HAHAHA WRONG.'")
        print("Oh wait. No. You're right...")
        print("'CORRECT.'")
        print("You have passed. The witch hands you the Kingslayer; a sword that has made kingdoms crumble.")
        print("Why she gave you the sword after a single physics question, I'm not sure. But I'd take it.")
        print("Ther witch leads you through a door in the back of the room and you walk out onto a lush field near your house.")
        print("You turn around to thank the witch but the cave is gone. You can only see the forest that is a few hundred yards out.")
        print("You head in the direction of where the bandits were going.")
        print("You reach their camp by nightfall and take shelter up in a tree further away from where they've stationed themselves.")
        midnightStrike(name)
        print("")

def midnightStrike(name):
    attack = ""
    while attack != "attack now" and attack != "wait":
        attack = raw_input("Do you attack now or wait until the following day? \n").lower().strip()

    if attack == "attack now":
        print("")
        print("You do something")
        print("")

    if attack == "wait":
        print("")
        print("You do something")
        print("")
    



### START GAME BELOW ###
### This basically starts everything. Everything is tied to this one function. Is that bad? Probably. I dunno. *shrug emoji* ###


storyIntro()