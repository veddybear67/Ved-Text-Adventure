# room.py
class Room:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.exits = {}        # direction -> Room
        self.character = None 
        self.shop = {}       
        self.item = None
        self.puzzle = None 
        self.locked = False
        self.lock_key = None   
    def set_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

    def set_character(self, character):
        self.character = character

    def set_shop(self, shop_items):
        self.shop = shop_items

    def set_item(self, item_name):
        self.item = item_name

    def set_puzzle(self, puzzle_name):
        self.puzzle = puzzle_name

    def lock(self, key_name):
        self.locked = True
        self.lock_key = key_name

    def unlock_with(self, inventory):
        """Try to unlock using player's inventory (list). Returns True if unlocked."""
        if not self.locked:
            return True
        if self.lock_key and self.lock_key in inventory:
            self.locked = False
            return True
        return False

    def describe(self):
        print(f"\n--- {self.name} ---")
        print(self.description)
        if self.character:
            print(f"You see {self.character.name} here.")
        if self.item:
            print(f"There is an item here: {self.item}")
        if self.shop:
            print("This place has a shop.")
        if self.puzzle:
            print("There is a puzzle to solve here.")
        if self.locked:
            print("This area appears to be locked.")
        if self.exits:
            exits_str = ", ".join(sorted(self.exits.keys()))
            print(f"Exits: {exits_str}")

