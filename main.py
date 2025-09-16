from room import Room
from character import Character


entrance = Room("Entrance", "You stand at the gates of the Chopz Arena.")
shop = Room("Shop", "A dimly lit shop full of strange goods.")
trap_room = Room("Trap Room", "A spiked floor lies ahead.")
riddle_room = Room("Riddle Room", "A glowing wall with words carved in it.")
mini_boss = Room("Mini-Boss Room", "A thug blocks the path.")
arena = Room("Arena", "The final stage. Mason awaits.")

# NEW Rooms
maze_room = Room("Maze Room", "You’re lost in twisting corridors.")
mirror_room = Room("Mirror Room", "Dozens of reflections confuse you.")
guardian_room = Room("Guardian Room", "A giant guardian blocks the way.")


entrance.set_exit("north", shop)
shop.set_exit("east", trap_room)
trap_room.set_exit("north", riddle_room)
riddle_room.set_exit("east", mini_boss)
mini_boss.set_exit("north", maze_room)
maze_room.set_exit("west", mirror_room)
mirror_room.set_exit("north", guardian_room)
guardian_room.set_exit("east", arena)


merchant = Character("Merchant", "Buy clippers to stand a chance!", False, "clippers")
thug = Character("Thug", "You ain’t passing without a fight!", True, weakness="clippers")
mason = Character("Mason", "JC Chopz, your time is up!", True, weakness="clippers")
guardian = Character("Guardian", "None shall pass unless you prove your strength!", True, weakness="food")

shop.character = merchant
mini_boss.character = thug
arena.character = mason
guardian_room.character = guardian

# --- Items ---
shop.item = "food"


trap_room.puzzle = "escape"
riddle_room.puzzle = "riddle"
maze_room.puzzle = "maze"
mirror_room.puzzle = "mirror"
guardian_room.puzzle = "guardian"


current_room = entrance
inventory = []
energy = 100


def solve_puzzle(room):
    global energy

    if room.puzzle == "escape":
        print("You must cross the spiked floor. Do you jump (j) or walk (w)?")
        move = input("> ").lower()
        if move == "j":
            print("You leapt safely across!")
        else:
            print("You got hurt! -30 energy.")
            energy -= 30

    elif room.puzzle == "riddle":
        print("Riddle: What has keys but can’t open locks?")
        answer = input("> ").lower()
        if "piano" in answer:
            print("Correct! The path glows open.")
        else:
            print("Wrong! You lose -20 energy.")
            energy -= 20

    elif room.puzzle == "maze":
        print("You’re in a maze! Choose left (l) or right (r).")
        choice = input("> ").lower()
        if choice == "l":
            print("You found the way out!")
        else:
            print("Dead end! -15 energy.")
            energy -= 15

    elif room.puzzle == "mirror":
        print("The mirrors whisper: 'Find the truth.' Break (b) or ignore (i)?")
        action = input("> ").lower()
        if action == "b":
            print("You smash the right mirror and a passage opens.")
        else:
            print("The illusions drain your mind! -25 energy.")
            energy -= 25

    elif room.puzzle == "guardian":
        print("The Guardian demands you show strength. Do you feed it food (f) or fight (fight)?")
        action = input("> ").lower()
        if action == "f" and "food" in inventory:
            print("The Guardian eats and lets you pass.")
        elif action == "fight":
            weapon = "clippers" if "clippers" in inventory else None
            result = guardian.fight(weapon)
            if not result:
                print("Game Over!")
                exit()
        else:
            print("You failed the trial! -40 energy.")
            energy -= 40



while True:
    current_room.describe()
    print(f"Energy: {energy}, Inventory: {inventory}")

    if current_room.character:
        current_room.character.talk()
        if current_room.character.item:
            choice = input("Buy item? (y/n) ").lower()
            if choice == "y":
                inventory.append(current_room.character.item)
                print(f"You got {current_room.character.item}!")

    if current_room == arena:
        weapon = "clippers" if "clippers" in inventory else None
        mason.fight(weapon)
        print("Thanks for playing!")
        break

    if current_room.puzzle:
        solve_puzzle(current_room)

    command = input("Move (north/south/east/west) or quit: ").lower()
    if command == "quit":
        print("Thanks for playing!")
        break
    else:
        next_room = current_room.get_exit(command)
        if next_room:
            current_room = next_room
        else:
            print("You can’t go that way.")
