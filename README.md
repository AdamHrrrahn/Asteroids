# Overview

I wrote this game as a start in learning about designing a running game.

The game that i wrote is a variation on asteroids. You are a ship that can rotate and accelerate forward and fire bullets. controls are as follows: w or up to accelerate, a or left to rotate left, d or right to rotate right, p to enter the pause menu up and down to navigate through menus, and space to fire or select an option in a menu. asteroids and enemy ships will periodically spawn in from the sides of the map. Asteroids move in a constant direction at a constant speed once spawned, and come in a variety of sizes with health corosponding to their size. When their health is depleted through coliding with your bullets or your ship (which also causees damage to your ship) they will drop up to a number of resource items that can be picked up by your ship. large asteroids will also spawn in smaller asteroids moving in a random direction from the point of the large asteroid's death. Enemy ships have controls for movement identical to the players, and will rotate to try to attack the player's ship, periodically firing a bullet. Both the player's ship and enemy ships have a shield that takes damage before the ship does and regenerates over time. Enemies drop a resource item on their death whose value is twice that of a resource item dropped by an asteroid. The player's ship has a cargo capacity and can only hold so many resource items at a time. there is a station at the center of the map that the player can land at by pressing the "L" button when within landing distance, which wil be denoted by a message showing at the bottom of the screen telling the player how to land. landind will pull up the station menu which has options for hte player to launch their ship and resume the game, repair their ship, sell their cargo, upgrade their ship, save their game, load their game, or quit the game. The upgrade, save, and load options will bring up another menu. The upgrade menu has a list of statistics for hte ship that can be improved, with the cost listed at the top, and a return option at the bottom. The save and load options will pull up a menu that has the three save files for the game, which will be initialized as empty when the game will be in stalled if I ever actually get around to compiling and releasing it, and show the level and money of the saved game. Saving will overwite the file an then return to the station screen while the loading a file will pull in the ship statistics from the save file and start the game. When starting the game, an intro screen describing gameplay and controls will be displayed, with a menu to start a new game, load a file, or quit the game. the pause menu also has the options to resume or quit the game.

My purpose for this was to learn the framework for writing a game in python as well as learn to handle the gameplay lood of a real time action game, as opposed to a turn based game like chess.

[Software Demo Video](https://youtu.be/LWZTcoU5XV8)

# Development Environment

I developed the game in the visual studio code IDE.

I wrote the program in the python language. i used the arcade library for the primary framework of the game, and used the random and math libraries for computations.

# Useful Websites

* [The Python Arcade Library](https://api.arcade.academy/en/)
* [Arcade: A Primer on the Python Game Framework](https://realpython.com/arcade-python-game-framework/#extras)

# Future Work

* I have noticed a bug where when an enemy ship spawns they sometimes turn away from the game screen and past the despawn line instead of turning in to face the player.
* The stats for the player's ship and the other objects in the game are not fully balanced out yet, but that will take a lot of time and trial and error to figure out.
* I would like to reformat the game so that instead of hte player ship moving around a small map that is entirely shown, that the player ship moves around a large map, with the display window being a small portion of the map centered on the player. The station would stay at the center of the map, and the stats of enemies and asteroids will be higher the farther from the station you get, but with equally increased rewards.
* After the previous is completed, I would add in a boss enemy that would spawn at set points on the map, with boss music, high health, more than 1 attack pattern, and significant resource drups upon defeat. said bosses may not respawn, or take a significant time to respawn.