# My first proper python text RPG
#Darius Caderyn Eames

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

###player set up###
class player:
    def _init_(self):
        self.job = ''
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
        self.gameover = False
myPlayer = player()

### Title Screen ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder untill written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command. play, help, quit.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder untill written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

    def title_screen():
        os.system('clear')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('       Welcome to my RPG text based game')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("                   |Play|                       ")
        print("                   |Help|")
        print("                   |Quit|")
        print("Special thanks to Btong for the tutorial on this game/'s creation.")
        print("Recreated By Darius Eames.")
        title_screen_selections()

    def help_menu():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                 Help menu')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("     |Use up, down, left, right to move.|                       ")
        print("         |Type command to do stuff.|")
        print("       |Use 'look' to inspect stuff.|")
        print("        |Try not to die. Good luck.|")
        title_screen_selections()

### Game functionality ###
def start_game():

    ### Map ###
    """
 1 2 3 4  
_________
| | | | |a
_________
| | | | |b
_________
| | | | |c
_________
| | | | |d
""" # player starts at d1

ZONENAME = ''
DESCRIPTION = 'description'
EXPLANATION = 'examine'
SOLVED = False
UP = 'up' or 'north'
LEFT = 'left' or 'west'
RIGHT = 'right' or 'east'
DOWN = 'down' or 'south'

solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
                 'b1': False,'b2': False,'b3': False,'b4': False,
                 'c1': False,'c2': False,'c3': False,'c4': False,
                 'd1': False,'d2': False,'d3': False,'d4': False,
                 }

zonemap = {
    'a1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: '',
        LEFT: '',
        RIGHT: 'a2',
        DOWN: 'b1',
    },
    'a2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: '',
        LEFT: 'a1',
        RIGHT: 'a3',
        DOWN: 'b2',
    },
    'a3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: '',
        LEFT: 'a2',
        RIGHT: 'a4',
        DOWN: 'b3',
    },
    'a4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: '',
        LEFT: 'a3',
        RIGHT: '',
        DOWN: 'b4',
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        LEFT: '',
        RIGHT: 'b2',
        DOWN: 'c1',
    },
    'b2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'a2',
        LEFT: 'b1',
        RIGHT: 'b3',
        DOWN: 'c2',
    },
    'b3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        LEFT: 'b2',
        RIGHT: 'b4',
        DOWN: 'c3',
    },
    'b4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        LEFT: 'b3',
        RIGHT: '',
        DOWN:  'c4',
    },
    'c1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        LEFT: '',
        RIGHT: 'c2',
        DOWN:  'd1',
    },
    'c2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        LEFT: 'c1',
        RIGHT: 'c3',
        DOWN:  'd2',
    },
    'c3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'b3',
        LEFT: 'c2',
        RIGHT: 'c4',
        DOWN: 'd3',
    },
    'c4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'b4',
        LEFT: 'c3',
        RIGHT: '',
        DOWN: 'd4',
    },
    'd1': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home. A small house next to a stream.',
        EXPLANATION: 'It is quite small. Good enough for a hobbet or midget.',
        SOLVED: False,
        UP: 'c1',
        LEFT: '',
        RIGHT: 'd2',
        DOWN: '' ,
    },
    'd2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'c2',
        LEFT: 'd1',
        RIGHT: 'd3',
        DOWN:  '',
    },
    'd3': {
        ZONENAME: '',
        DESCRIPTION:  'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'c3',
        LEFT:  'd2',
        RIGHT: 'd4',
        DOWN:  '',
    },
    'd4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXPLANATION: 'examine',
        SOLVED: False,
        UP: 'c4',
        LEFT: 'd3',
        RIGHT: '',
        DOWN: '',
        },
    }
### Game Interactivity ###
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "##############################")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action. Please try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where do you want to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location](UP)
        movement_handler()
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location](LEFT)
        movement_handler()
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location](RIGHT)
        movement_handler()
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location](DOWN)
        movement_handler()

def movement_handler(destination):
    print("\n" + "You have moved to the "  + destination + ".") 
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location] [SOLVED]:
        print ('You have already exhuasted this area.')
    else:
        print("You can trigger puzzel here.")
    
### Game Functionality ###
def start_game():
    return

def main_game_loop():
    while myPlayer.gameover is False:
        prompt()
    #here handle once goal is completed

def setup_game():
    os.system('clear')

#NAME collecting
    question1 = "Hello, player. What is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(": ")
    myPlayer.name = player_name
        
#JOB Handling
    question2 = "What role do you want to play?\n"
    question2added = "You can only play as a warrior, priest or mage.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_job = input(": ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a" + player_job + "!\n")
    
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a" + player_job + "!\n")

        #Class STATISTICS
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20

    elif myPlayer.job is 'mage':
        self.hp = 60
        self.mp = 120

    elif myPlayer.job is 'priest':
         
        self.hp = 80
        self.mp = 90

   #Game INTRODUCTION
    question3 = "Welcom, " + player_name + player_job + ".\n" 
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(": ")
    myPlayer.name = player_name

#NPC speech
    speech1 = "Welcome to this fantasy world!"
    speech2 = "I hope that it greets you well."
    speech3 = "Just don\'t die of stupidity."
    speech4 = "heheheheh..!"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.5)

    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.5)

    os.system('clear')
    print("###################")
    print("LET THE GAME BEGIN!")
    print("###################")
    main_game_loop()

title_screen()




