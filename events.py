import random
from characters import NPC

def trigger_event(player, location):
    # Randomly decide if an event occurs (30% chance)
    if random.random() < 0.3:
        event_type = random.choice(["treasure", "npc_encounter", "trap"])
        if event_type == "treasure":
            item = random.choice(["gold coin", "magic ring", "ancient scroll"])
            print(f"You discover a hidden treasure! You found a {item}.")
            player.add_item(item)
        elif event_type == "npc_encounter":
            npc = NPC(name="Mysterious Stranger")
            print("A mysterious stranger appears!")
            npc.interact(player)
        elif event_type == "trap":
            damage = random.randint(5, 20)
            print("Oh no! You triggered a trap!")
            player.take_damage(damage)
