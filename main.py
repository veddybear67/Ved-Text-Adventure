from room import Room
from character import Character, Enemy

# --- Rooms ---
town = Room("Town", "The central hub with shops and chatter.")
forest = Room("Forest", "A quiet place with tall trees.")
cave = Room("Cave", "A damp and dark cave.")
village = Room("Village", "A peaceful community of NPCs.")
castle = Room("Castle", "Guards watch you closely.")
arena = Room("Arena", "The final showdown spot!")

# --- Links ---
town.link_room(forest, "north")
forest.link_room(cave, "east")
cave.link_room(village, "south")
village.link_room(castle, "west")
castle.link_room(arena, "north")

# --- Characters ---
shopkeeper = Character("Bob the Shopkeeper", "A friendly merchant.")
shopkeeper.set_conversation("I sell swords and food!")
guard = Character("Guard", "Looks serious.")
guard.set_conversation("Stay safe, traveler.")
villager = Character("Anna", "A smiling villager.")
villager.set_conversation("Our village is calm, but danger looms ahead.")

mason = Enemy("Mason", "Your rival with a baseball bat.")
mason.set_conversation("JC Chopz, you’ll never beat me!")
mason.set_weakness("Clippers")

town.set_character(shopkeeper)
forest.set_character(guard)
village.set_character(villager)
arena.set_character(mason)

# --- Shops ---
town.set_shop({"Food": 5, "Clippers": 15})
cave.set_shop({"Potion": 10})
village.set_shop({"Shield": 12})

# --- Player ---
inventory = []
coins = 20
current_room = town

# --- Game Loop ---
while True:
    current_room.get_details()
    if current_room.character:
        current_room.character.describe()

    print(f"\nCoins: {coins} | Inventory: {inventory}")
    command = input("\nCommand (north/south/east/west, talk, shop, fight, quit): ").lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk" and current_room.character:
        current_room.character.talk()

    elif command == "shop" and current_room.shop:
        print("\nItems for sale:")
        for item, price in current_room.shop.items():
            print(f"- {item}: {price} coins")
        choice = input("Buy what? (or 'exit'): ").title()
        if choice in current_room.shop:
            price = current_room.shop[choice]
            if coins >= price:
                coins -= price
                inventory.append(choice)
                print(f"You bought {choice}!")
            else:
                print("Not enough coins.")
        elif choice != "Exit":
            print("Item not found.")

    elif command == "fight" and isinstance(current_room.character, Enemy):
        weapon = input("Fight with what? ").title()
        if weapon in inventory:
            if current_room.character.fight(weapon):
                print("You win! JC Chopz has defeated Mason!")
                break
            else:
                break
        else:
            print("You don’t have that item!")

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid command.")
