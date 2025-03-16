# world.py
import random

class Location:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits  # List of available directions

class World:
    DIRECTIONS = ['north', 'south', 'east', 'west']
    
    def __init__(self, size=5):
        self.size = size  # Define the world as a grid of locations
        self.grid = {}
        self.generate_world()
        
    def generate_world(self):
        for x in range(self.size):
            for y in range(self.size):
                name = f"Room ({x}, {y})"
                description = self.generate_description(x, y)
                exits = self.generate_exits(x, y)
                self.grid[(x, y)] = Location(name, description, exits)
                
    def generate_description(self, x, y):
        descriptors = ["dark", "mysterious", "quiet", "stormy", "ancient"]
        return f"A {random.choice(descriptors)} room located at coordinates ({x}, {y})."
    
    def generate_exits(self, x, y):
        exits = []
        if x > 0:
            exits.append("west")
        if x < self.size - 1:
            exits.append("east")
        if y > 0:
            exits.append("north")
        if y < self.size - 1:
            exits.append("south")
        return exits
    
    def get_start_location(self):
        # Start at a random location in the grid
        start_coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        return self.grid[start_coords]
    
    def move(self, current_location, direction):
        # Find the current location coordinates
        current_coords = None
        for coords, location in self.grid.items():
            if location == current_location:
                current_coords = coords
                break
        if not current_coords:
            return None
        
        x, y = current_coords
        if direction == "north":
            new_coords = (x, y - 1)
        elif direction == "south":
            new_coords = (x, y + 1)
        elif direction == "east":
            new_coords = (x + 1, y)
        elif direction == "west":
            new_coords = (x - 1, y)
        else:
            return None
        
        if new_coords in self.grid:
            return self.grid[new_coords]
        else:
            return None
