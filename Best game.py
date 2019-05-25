import time

#Small intro and starting info
print ("""The following is info on your character.
Remember if you die you will have to restart. In
this game you need common sense to survive or not.
""")
#Character info
name= input("Name:")
age= input("Age:")
gender= input("Gender:")
kind= input("Species E.g troll:")
promt=("Welcome")

#Random scenarios
import random
foo = random.randint(1,2)

if foo == 1:
    scenario = "an enchanted forest"

if foo == 2:
    scenario = "an abandoned farm"


while True:
    life = 1
    if life == 1:
        print ("""%s, %s. You are a %s year old %s, %s.
You are moving through %s.There is a broken structure to the west
and a hole to the north.
""" %(promt, name, age, gender, kind, scenario))
        user = input("Where do you go? ")

    if "west" in user or "broken" in user or "building" in user or "structure" in user:
        print("""You walk up to a hole in the wall of the structure.
in the structure, you notice a hatch to your right,
a fridge to your left, against a wall and door straight
ahead of you.""")
        user = input("What do you do? ")

        if "left" in user or "fridge" in user:
            print ("""You go up to the fridge. It is a shiny silver with a bit of rust on the edges.
""")
            user = input("Do you open it? ")
            if "yes" in user or "open" in user:
                print ("""You open the fridge as a light of the fridge fills the dim room.
You smell a horrific stench. You notice that the fridge is filled
with a black meat that is almost unrecognisable. """)
                user = input("Where do you go to the hatch or the door? ")

            if "no" in user or "don\'t" in user:
                print("You turn around.")
                user = input("Do you go to the hatch or the door? ")

        if "hatch" in user or "right" in user:
            print ("""You walk up to the hatch and open it. It is dark
inside.""")
            user = input("Do you jump in? ")
            if "yes" in user or "jump" in user:
                life = 0
                print("""You fall down but your fall was stopped short
by a concrete floor.
""")
            if "no" in user or "not" in user or "away" in user:
                life = 0
                print ("""As you turn around, you hear a loud screetch.
You notice a larg furry creature running up to you.
It quickly pushes you into the open hatch.
Your fall was stopped short of a concrete floor.
""")
        if "door" in user or "straight" in user:
            print("""You go to the door. On the way you almost trip over somthing,
you look to see what it is but it is gone. You open the door with a creak.
On the other side of the door you see a lot of plants and it is in a glass
structure. There is a large strange green plant to your left and a glass
sliding door ahead of you.
""")
            user = input("Where do you go? ")
            if "plant" in user or "left":
                print("""As you walk up to the plant, somthing grabs your legs.
One of the plant\'s roots has grabbed your anckle. The plant lifts you up to a
large bulb. The bulb opens up and swallows you. You pass out from the stress.
When you wake you notice that the plant is shredded and a green goo is on the
floor. The corpse of the plant has bits of fur on the roots and ripped bulb.
You walk up to the glass door and it slids open with ease. You have made it
through alive, congrats! You win!
""")
                break
            
            if "door" in user or "straight" in user or "ahead" in user or "forward" in user:
                life = 0
                print("""You walk up to the door, it slides open with ease. You hear a familiar
screetch behind you. You turn around a large furry creature followed you through the door.
A root on the floor grabs the monster. The root lifts the creature towards a large bulb which
opens up and swallows the creature whole. The monster screams as it is being consumed.
A few seconds later the bulb explodes. The monster burst forth in rage. It stares at you with
murderous intent. It charges at you and rips you apart.
""")
        
    if "north" in user or "hole" in user:
        life = 0
        print("""As you walk up to the hole you slip and fall in.
At the bottom you hit a soft sand and slowly
sink to your death.
""")
        
    if life == 0:
        print("You died")
        promt = ("Welcome back")

        
    
        import random
        p = random.randint(1,4)

        if p == 1:
            print ("""You suck at this game.
""")

        if p== 2:
            print ("""It is common sense that this game requires common sense.
""")

        if p == 3:
            print ("""This is just a game, not science!
""")

        if p == 4:
            print ("""If this was life I bet you'd suck at that too.
""")

    
        user = input("Restart?")
        if "no" in user or "don\'t" in user or "not" in user or "nah" in user:
            print("Good bye. Respawn soon!")
            break

        
