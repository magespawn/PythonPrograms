#DnD helper
#Darius Eames

#Thaco function
#Global lists
#Main campaign
#Random encounter
import pickle
class Player:
    def __init__(self, name):
        self.name = name
        self.age = 16
        self.maxhealth = 100
        self.health = self.maxhealth

def nameInputAsk():
    print("What is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    
nameInputAsk()
Save = Player(PlayerIG.name)
pickle.dump(Save, open("Save File", "wb"))
