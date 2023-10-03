from random import randint
from elements import *

ALL_ELEMS = [Fire, Water, Air, Earth, Aroma, Dust, Clay, Lava, Stone, Sand]

GAME.elements = get_base_elems(GAME.window)
for elem in GAME.elements:
    GAME.all_imgs[elem] = GAME.canvas.create_image(
        randint(2*GAME.margin, GAME.w-2*GAME.margin), 
        randint(2*GAME.margin, GAME.w-2*GAME.margin), 
        image=elem.img[GAME.curr_texture_pack])

'''
lambda usage
'''
# Clear manu: on click delete all elements
GAME.sett.mainmenu.add_command(label='Clear', command=lambda: GAME.canvas.delete('all'))
#GAME.sett.duplicates_menu.add_command(label='Yes', command=allow)
#GAME.sett.duplicates_menu.add_command(label='No', command=disallow)
    
GAME.launch()