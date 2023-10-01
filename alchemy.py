from tkinter import *
from random import randint


class Interface:
    def __init__(self) -> None:
        # create window
        self.window = Tk()
        self.h,self.w = 600,600
        self.margin = 50
        self.window.geometry(f'{self.w}x{self.h}')
        self.window.title('Алхимия')

        self.canvas = Canvas(self.window, width=self.w, height=self.h)
        self.canvas.pack()

    def get_init_elements(self):
        self.elements = [Fire(), Water(), Earth(), Air()]
        for elem in self.elements:
            img = self.canvas.create_image(
                randint(self.margin,self.w-self.margin), 
                randint(self.margin,self.w-self.margin), 
                image=elem.img)
            
    def move(self,event):
        images_id = self.canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)

        if len(images_id)==2:
            elem_id_1, elem_id_2 = images_id[0], images_id[1]
            element1 = self.elements[elem_id_1 - 1]
            element2 = self.elements[elem_id_2 - 1]

            new_element = element1 + element2
            if new_element:
                if new_element not in self.elements:
                    self.canvas.create_image(event.x + 20, event.y + 20, image=new_element.img)
                    self.elements.append(new_element)
                    #print(self.elements)

        self.canvas.coords(images_id, event.x, event.y)

    def launch(self):
        # mouse control
        self.window.bind('<B1-Motion>', self.move)
        # window launch
        self.get_init_elements()
        self.window.mainloop()


# create window
game = Interface()


# Elements
class Fire:
    img = PhotoImage(file=r'img/fire.png').subsample(5,5)

class Water:
    img = PhotoImage(file=r'img/water.png').subsample(5,5)

    def __add__(self, other):
        if isinstance(other, Air):
            return Aroma
        
        if isinstance(other, Earth):
            return Clay

class Earth:
    img = PhotoImage(file=r'img/earth.png').subsample(5,5)
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust
        
        if isinstance(other, Water):
            return Clay

class Air:
    img = PhotoImage(file=r'img/air.png').subsample(5,5)

    def __add__(self, other):
        if isinstance(other, Water):
            return Aroma
        if isinstance(other, Earth):
            return Dust

class Aroma:
    img = PhotoImage(file=r'img/aroma.png').subsample(5,5)
class Dust:
    img = PhotoImage(file=r'img/dust.png').subsample(5,5)
class Clay:
    img = PhotoImage(file=r'img/clay.png').subsample(5,5)


game.launch()