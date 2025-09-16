class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.character = None
        self.item = None
        self.locked = False
        self.puzzle = None

    def set_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

    def describe(self):
        print(f"\n--- {self.name} ---")
        print(self.description)
        if self.character:
            print(f"You see {self.character.name} here.")
        if self.item:
            print(f"You see {self.item} on the ground.")
        if self.locked:
            print("The door is locked.")
        if self.puzzle:
            print("There’s a puzzle here!")
