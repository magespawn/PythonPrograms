#Created by Darius Caderyn Eames
#Text based RPG 

import random
import time
import sys
life = 1
#type function
def type(text, delay):
    for beep in text:
        print(beep, end = "")
        sys.stdout.flush()
        time.sleep(delay)

#age function
def age():
    global Age
    while True:
        try:
            Age = input("Character age: ")
            Age = int(Age)
            break
        except ValueError:
            type("Please enter a valid number. ", 0.02)
     
#gender function
def gender():
    global Gender
    Gender = ""
    while Gender != "male" and Gender != "female":
        Gender  = input("Gender. (male or female): ").lower()
    return Gender

#spiecies function
def kind():
    global Kind
    Kind = ""
    while Kind != "human" and Kind != "troll" and Kind != "elf" and Kind != "dwarf" and Kind != "hobbit" and Kind != "peacock":
        Kind  = input("What are you? (Human, troll, elf, dwarf or hobbit): ").lower()
    return Kind

#Restart function

#Easter egg function
    
#Introduction
print("""###################################""")
time.sleep(0.1)
type("""#Hello, and welcome to my RPG.                                      #
#I hope that you enjoy the game. The game is linear,    #
#and it is mostly story based. Good luck.                         #
""", 0.03)
time.sleep(0.1)
print("""###################################
\n""")
time.sleep(2)
type("What is your name player?\n",0.02)
Plrname = input("")
type("Hmm... {}. ".format(Plrname), 0.07)
time.sleep(2)

#Adds abit of flavour text
Asd = random.randint(0,3)
Sayings = ["That is a nice name. ", "I wouldn't name my child that. ", "Wow! wierd name! ", ""]
Funintro = (Sayings[Asd])
type("{}".format(Funintro), 0.02)
time.sleep(1)
type ("Anyway let's start the game.\nType in the traits you want your character to have.\n",0.02)
time.sleep(0.5)
#character specs
print("""

###############################""")
kind()
time.sleep(0.5)
gender()
time.sleep(0.5)
Name = input("Character name: ")
time.sleep(0.5)
age()
print("""###############################
\n""")
time.sleep(1)

#Turns Age positive
if Age < 0:
        Age = Age * -1	
###Character trait summary function
def charactersum():
    if Kind == "peacock":
        print("""Ok %s, so you are a %s year old %s, %s.
Oh! Wait, so is this an alpa test?
\n"""%(Name, Age, Gender, Kind ))
        time.sleep(4)
    else:
        print("""Ok %s, so you are a %d year old %s, %s.
\n"""%(Name, Age, Gender, Kind ))
        time.sleep(4)

#Character trait summary
charactersum()

#Main scenarios
#Main game scenario1
def scenario1():
    type("""You are a stow-away on a cargo ship, heading away
from a mining colony. You were a slave there. You
are trying to regain your freedom but your slave
marks make it exceptionaly hard... 
\n""",0.02)
    time.sleep(6)
    type("""You have hidden yourself in a crate. It is empty
except for yourself and some dust. You have nothing
except for the clothes on your back. There is a hole 
in the crate big enough to peak through. You hear
foot steps outside the crate.
\n""",0.02)
    time.sleep(6)
    type("""You have FOUR options; 
1. Peak out the crate, through the hole.
2. Wait for the foots steps to pass.
3. Throw somthing out of the crate.
4. Call out to the entity. 
\n """,0.02)
    time.sleep(2)
    type("""What do you do?
\n""",0.04)
    response = input("").lower()
    print(" ")
    #If option 1 is selected
    if "1" in response or "peak" in response or "hole" in response:
        type("""You see a person walking outside the crate. It is a guard!
He is patrolling in the room that you are in. He is busy 
inspecting some of the cargo. After looking at some of  
the items, he tenses his muscles as he stretches and     
gives off a sigh. He turns around, glances at the crate  
you are in. Just before he can take a look at your crate, a    
voice shouts a name in the distance. This grabs the      
guards attention and he walks away out of view.
\n""", 0.02)
        restart()
    #If option 2 is selected
    if "2" in response or "wait" in response:
        type("""You wait in the crate patiently. After a few minutes,
of what sound like shuffling through items, the
foot steps move away out of ear shot.
\n""",0.02)
        life = 0
    #If option 3 is selected
    if "3" in response or "throw" in response:
        type ("""You don't have anything with weight to throw
but you do have your clothes. A shirt and a pair
of pants.
\n""",0.02)
        life = 1
    #If option 4 is selected
    if "4" in response or "call" in response or "entity" in response:
        type("What do you call out?\n",0.02)
        Response = input("")
        type ("""You call out to the entity, \"{}\"
The entity walks up to the crate.""".format(Response), 0.02)
       
#Main game scenario2
def scenario2():
    type("""
You are a secuirity gaurd on a cargo ship, heading
towards a ship construction planet. The cargo that
you are guarding is extremely valuable and very
essential to space ship construction.
 \n""",0.02)


#Random selection between the 2 scenarios
Scenario = random.randint(1,1)
if Scenario == 1:
    scenario1()

if Scenario == 2:
    scenario2()






