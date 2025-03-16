from world import World
from characters import Player
from events import trigger_event
import sys

def game_loop():
    # Initialize the world and player
    world = World(size=5)  # Change size for larger worlds
    player_name = input("Enter your adventurer's name: ")
    player = Player(player_name)
    
    print("\nWelcome to Adventure Quest, {}!".format(player.name))
    print("Your adventure begins...\n")
    
    current_location = world.get_start_location()
    
    while True:
        # Display current location details
        print("You are at: {}".format(current_location.description))
        print("Exits: " + ", ".join(current_location.exits))
        
        # Trigger a random event at the location
        trigger_event(player, current_location)
        
        # Get player input for direction or command
        command = input("\nWhich direction do you want to go? (or type 'quit' to exit): ").strip().lower()
        if command == 'quit':
            print("Thanks for playing Adventure Quest!")
            sys.exit(0)
        
        # Move the player if the exit is available
        new_location = world.move(current_location, command)
        if new_location:
            current_location = new_location
        else:
            print("You can't go that way! Try another direction.")

if __name__ == "__main__":
    game_loop()
