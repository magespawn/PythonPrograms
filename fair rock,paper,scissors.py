bar = input("Rock, paper, scissors:")
foo = 0
import random
foo = random.randint (0,3)

if foo == 1:
    print("Paper")
if foo == 2:
    print("Rock")
if foo == 3:
    print("Scissors")


if bar == "rock" or bar == "Rock" and foo == 1:
    print (" Hah! I win!")
if bar == "paper" or bar == "paper" and foo == 1:
    print ("Great. It is a tie. I will win next round!")
if bar == "scissors" or bar == "Scissors" and foo == 1:
    print("I hate paper.")

if bar == "rock" or bar == "Rock" and foo == 2:
    print("It is like we are cave men. Fighting with stones.")
if bar == "paper" or bar == "Paper" and foo == 2:
    print("A perfect birthday gift. A hardened, mineral ball wraped in dried, tree pulp.")
if bar == "scissors" or bar == "Scissors" and foo == 2:
    print("I destroyed you!")

if bar == "rock" or bar == "Rock" and foo == 3:
    print("Never bring scissors to a rock fight!")
if bar == "paper" or bar == "Paper" and foo == 3:
    print("I love winning!")
if bar == "scissors" or bar == "Scissors" and foo == 3:
    print("Not the straightest thing I have ever seen.")

 
