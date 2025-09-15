class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = {}
        self.character = None
        self.shop = {}

    def link_room(self, room, direction):
        """Link this room to another in a direction"""
        self.linked_rooms[direction] = room

    def set_character(self, character):
        self.character = character

    def set_shop(self, shop_items):
        self.shop = shop_items

    def get_details(self):
        print(f"\n-- {self.name} --")
        print(self.description)
        for direction in self.linked_rooms:
            print(f"{direction.title()} -> {self.linked_rooms[direction].name}")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can’t go that way.")
            return self
