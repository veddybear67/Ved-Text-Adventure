import random, sys
from room import Room
from character import Character, Enemy


player = {"name": "JC Chopz", "health": 100, "coins": 30, "inventory": []}


entrance = Room("Entrance","The city gate.")
market   = Room("Market","Busy stalls and merchants.")
bakery   = Room("Bakery","Fresh bread smells amazing.")
workshop = Room("Workshop","Old machines and tools.")
alley    = Room("Alley","Dark and suspicious.")
library  = Room("Library","Dusty books everywhere.")
maze     = Room("Maze","Twisting confusing walls.")
mirror   = Room("Mirror Hall","Endless reflections.")
guardian = Room("Guardian Chamber","A huge iron guardian.")
arena    = Room("Arena","The final showdown with Mason!")

entrance.set_exit("north", market)
market.set_exit("south", entrance); market.set_exit("east", bakery); market.set_exit("west", workshop); market.set_exit("north", alley)
bakery.set_exit("west", market); workshop.set_exit("east", market)
alley.set_exit("south", market); alley.set_exit("north", library)
library.set_exit("south", alley); library.set_exit("north", maze)
maze.set_exit("south", library); maze.set_exit("east", mirror)
mirror.set_exit("west", maze); mirror.set_exit("north", guardian)
guardian.set_exit("south", mirror); guardian.set_exit("north", arena)
arena.set_exit("south", guardian)

#
market.set_shop({"Apple":3,"Bread":5})
bakery.set_shop({"Cake":8})
workshop.set_shop({"Clippers":25})
library.set_shop({"Old Map":10})

# Characters
market.set_character(Character("Rico","A hustler.","Cheap trinkets!"))
bakery.set_character(Character("Lani","Friendly baker.","Cake for strength."))
workshop.set_character(Character("Tinker","Old mechanic.","Maybe Clippers?"))
library.set_character(Character("Elira","Wise librarian.","Solve my riddle."))
guardian.set_character(Enemy("Guardian","Iron protector.","None shall pass!","Guardian Key",150,20))
arena.set_character(Enemy("Mason","Final boss with a bat.","You’re done!","Clippers",200,25))

# Puzzles
market.set_puzzle("guess")    # easy
library.set_puzzle("riddle")  # medium
maze.set_puzzle("maze")       # harder
mirror.set_puzzle("mirror")   # hardest
guardian.set_puzzle("guardian")


def show_status(room):
    print(f"\n-- {room.name} --\n{room.description}")
    print(f"HP:{player['health']} | Coins:{player['coins']} | Items:{player['inventory']}")

def shop(room):
    if not room.shop: print("No shop here."); return
    for item,price in room.shop.items(): print(f"{item} ({price}c)")
    choice=input("Buy what? ").title()
    if choice in room.shop and player["coins"]>=room.shop[choice]:
        player["coins"]-=room.shop[choice]; player["inventory"].append(choice)
        print(f"You bought {choice}")
    else: print("Can't buy.")

def puzzle(room):
    if room.puzzle=="guess":
        if int(input("Guess 1-5: "))==random.randint(1,5): player["coins"]+=5; print("Win 5c")
        else: print("Wrong!")
    elif room.puzzle=="riddle":
        ans=input("I speak w/o mouth, echo back. What am I? ").lower()
        if "echo" in ans: print("Correct! Take this Old Map."); player["inventory"].append("Old Map")
        else: player["health"]-=10; print("Wrong -10HP")
    elif room.puzzle=="maze":
        path=["left","right","left"]
        for step in path:
            if input("Go left or right? ").lower()!=step: player["health"]-=15; print("Wrong turn -15HP"); return
        print("Maze cleared!")
    elif room.puzzle=="mirror":
        if input("Pick real mirror A/B/C/D: ").upper()=="C": print("Correct +15c"); player["coins"]+=15
        else: player["health"]-=20; print("Wrong mirror -20HP")
    elif room.puzzle=="guardian":
        if "Clippers" in player["inventory"]: print("You cut Guardian’s wires. He drops Guardian Key."); player["inventory"].append("Guardian Key")
        else: player["health"]-=25; print("Guardian smashes you -25HP")
    room.puzzle=None

def fight(enemy):
    while player["health"]>0 and enemy.health>0:
        if "Clippers" in player["inventory"]:
            print("Critical strike with Clippers!"); enemy.health=0
        else:
            enemy.health-=20; player["health"]-=enemy.damage
            print(f"EnemyHP:{enemy.health}, YourHP:{player['health']}")
    if enemy.health<=0: print(f"You beat {enemy.name}!")
    else: print("You lost..."); sys.exit()

# ---------- Game Loop ----------
current=entrance
print("Welcome to JC Chopz Adventure!")

while True:
    if player["health"]<=0: print("You collapse. Game over."); break
    show_status(current)

    if current.character: current.character.talk()
    if current.item: 
        if input("Pick up item? (y/n) ").lower()=="y": player["inventory"].append(current.item); current.item=None
    if current.puzzle: puzzle(current)
    if current is arena: fight(current.character); print("JC Chopz wins against Mason!"); break

    print("\nCommands: north/south/east/west | shop | inv | quit")
    cmd=input("> ").lower()

    if cmd=="quit": break
    elif cmd=="shop": shop(current)
    elif cmd=="inv": print(player["inventory"])
    elif cmd in ["north","south","east","west"]:
        next_r=current.get_exit(cmd)
        if next_r: current=next_r
        else: print("Can't go that way.")
    else: print("Not a command.")


