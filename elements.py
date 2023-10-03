from tkinter import PhotoImage
from settings import *
from config import GAME

# load the current game window
window = GAME.window

def get_base_elems(w):
    '''
    Returns a list of 4 base element classes instances
    '''
    return [Fire(), Water(), Earth(), Air()]


# decorator for duplicates
'''
decorator usage
'''
def _check_class_duplicates(cls):
    '''
    Checks gwhether or not duplicates are currently allowed. 
    If not, then it overrides the classes' instance creation by allowing only singletons.
    '''

    def decorator_init(self,*args):
        self._instance = None

        if not GAME.allow_duplicates:
            def __new__(self):
                if self._instance is None:
                    self._instance = object.__new__(self)
                    return self._instance
                
        self.__new__ = __new__
            
        #print(self._instance)
    
    decorator_init(cls)
    return cls



# Element classes containing reference images and element adding behaviour
@_check_class_duplicates
class Fire:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/fire.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/fire.png').subsample(4,4)}

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        

@_check_class_duplicates
class Water:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/water.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/water.png').subsample(5,5)}

    def __add__(self, other):
        if isinstance(other, Air):
            return Aroma()
        if isinstance(other, Earth):
            return Clay()

        if isinstance(other, Lava):
            return Stone()
        if isinstance(other, Stone):
            return Sand()

@_check_class_duplicates
class Earth:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/earth.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/earth.png').subsample(8,8)}

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Water):
            return Clay()
        if isinstance(other, Fire):
            return Lava()

@_check_class_duplicates
class Air:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/air.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/air.png').subsample(5,5)}

    def __add__(self, other):
        if isinstance(other, Water):
            return Aroma()
        if isinstance(other, Earth):
            return Dust()

@_check_class_duplicates
class Aroma:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/aroma.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/aroma.png').subsample(3,3)}
@_check_class_duplicates
class Dust:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/dust.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/dust.png').subsample(3,3)}
@_check_class_duplicates
class Clay:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/clay.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/clay.png').subsample(10,10)}

@_check_class_duplicates
class Lava:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/lava.png').subsample(2,2),
           'hd' : PhotoImage(file=r'img/hd_pack/lava.png').subsample(15,15)}

    def __add__(self, other):
        if isinstance(other, Water):
            return Stone()

@_check_class_duplicates    
class Stone:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/stone.png').subsample(5,5),
           'hd' : PhotoImage(file=r'img/hd_pack/stone.png').subsample(3,3)}

    def __add__(self, other):
        if isinstance(other, Water):
            return Sand()

@_check_class_duplicates        
class Sand:
    img = {'clip_art' : PhotoImage(file=r'img/clip_art_pack/sand.png').subsample(6,6),
           'hd' : PhotoImage(file=r'img/hd_pack/sand.png').subsample(25,25)}
