# j4f---adventure-quest
# Adventure Quest

Welcome to **Adventure Quest**, a text-based adventure game built in Python! In this project, you'll explore a procedurally generated world filled with mysterious locations, quirky characters, and unexpected events that make every playthrough unique.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Extending the Project](#extending-the-project)
- [License](#license)

## Overview

**Adventure Quest** is designed as a fun, high-level Python project that showcases object-oriented programming, modular design, and procedural world generation. Every time you play, the game generates a new world with unique descriptions, challenges, and rewards, ensuring an exciting and unpredictable adventure.

## Features

- **Procedural World Generation:** Create a grid-based world with randomly generated descriptions and available exits.
- **Random Events:** Encounter treasures, NPC interactions, and traps that impact your adventure.
- **Character Interactions:** Engage with a variety of characters including the player and non-player characters (NPCs).
- **Modular Design:** The project is structured into multiple modules for clear organization and ease of expansion.

## Project Structure

```plaintext
Adventure Quest/
│
├── main.py         # Entry point for the game, handles the main game loop and user input.
├── world.py        # Contains logic for procedural generation of locations.
├── characters.py   # Defines classes for the player and NPCs.
├── events.py       # Manages random events and encounters.
└── utils.py        # Utility functions for random generation and text formatting.
