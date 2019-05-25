name = input ("Name:")
foo = input("Rock, Paper, Scissors: ")
if foo == "Rock" or foo == "rock":
    print("Paper. I win, %s" %(name))

if foo == "Paper" or foo == "paper":
    print("Scissors. I win, %s" %(name))

if foo == "Scissors" or foo == "scissors":
    print ("Rock. I win, %s" %(name))

if foo != "Scissors" and foo != "scissors" and foo != "Rock" and foo != "rock" and foo != "Paper" and foo != "paper":
    print ("That isn\'t appart of the game, %s!" %(name))

