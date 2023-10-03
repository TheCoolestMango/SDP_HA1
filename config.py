from settings import *
from tkinter import Tk, Canvas

class Interface:
    def __init__(self) -> None:
        # create window
        self.window = Tk()
        self.h,self.w = 600,600
        self.margin = 50
        self.window.geometry(f'{self.w}x{self.h}')
        self.window.title('Алхимия')

        # create canvas to display textures
        self.canvas = Canvas(self.window, width=self.w, height=self.h)
        self.canvas.pack()

        self.curr_texture_pack = TEXTURES[0]
        self.all_imgs = {}

        self.allow_duplicates = False

            
    def clip_art(self):
        self.curr_texture_pack = TEXTURES[0]
        for elem in self.elements:
            self.retexture(self.all_imgs[elem], elem)

    def hd(self):
        self.curr_texture_pack = TEXTURES[1]
        for elem in self.elements:
            self.retexture(self.all_imgs[elem], elem)
            
    def allow(self):
        self.allow_duplicates = True

    def disallow(self):
        self.allow_duplicates = False


    def get_settings_menu(self):
        # top menu
        self.sett = Settings(self.window, [self.clip_art, self.hd, self.allow, self.disallow])
        self.window.config(menu=self.sett.mainmenu)


    def retexture(self, img_container, elem):
        self.canvas.itemconfig(img_container, image=elem.img[self.curr_texture_pack])

            
    def move(self,event):
        images_id = self.canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)

        if len(images_id)==2:
            elem_id_1, elem_id_2 = images_id[0], images_id[1]
            element1 = self.elements[elem_id_1 - 1]
            element2 = self.elements[elem_id_2 - 1]

            new_element = element1 + element2
            #print(new_element)
            if new_element:
                self.add_new_element(new_element,event)
                    #print(self.elements)

        self.canvas.coords(images_id, event.x, event.y)


    def add_new_element(self, new_element,event):
        if new_element not in self.elements:
            self.all_imgs[new_element] = self.canvas.create_image(event.x+20, event.y+20, image=new_element.img[self.curr_texture_pack])
            self.elements.append(new_element)



    def launch(self):
        # mouse control
        self.window.bind('<B1-Motion>', self.move)
        # window launch
        self.window.mainloop()

GAME = Interface()
GAME.get_settings_menu()