# Alchemy game
__________________________

## Installation and launch
* Clone this repository onto your PC
* Launch terminal from this repository folder
* Type the following command to launch game:
  ``` python3 launch.py ```
* Control the elements with mouse

## Repository description
The ```img``` folder contains two available texture packs for all currently implemented elements. Texture pack can be changed in-game using the top-menu.\
 ``` settings.py ``` creates a Settings class for top-menu creation\
 ``` config.py ``` creates an Interface class for creating the game window and defining element combination logic\
 ``` elements.py``` creates a class for each element and a decorator function to disallow element duplication\
 ``` launch.py ``` launches the game, spawns four base elements and adds a clear menu option using a lambda-function
