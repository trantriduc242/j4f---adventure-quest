import random

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    
    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.inventory = []
    
    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} took {amount} damage and now has {self.health} health.")
        
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} found a {item}!")

class NPC(Character):
    def __init__(self, name, health=50):
        super().__init__(name, health)
    
    def interact(self, player):
        # A simple interaction: the NPC might help or harm the player
        action = random.choice(["help", "harm"])
        if action == "help":
            print(f"{self.name} offers you a healing potion!")
            player.health = min(player.health + 20, 100)
            print(f"{player.name}'s health is now {player.health}.")
        else:
            damage = random.randint(5, 15)
            print(f"{self.name} attacks you!")
            player.take_damage(damage)
