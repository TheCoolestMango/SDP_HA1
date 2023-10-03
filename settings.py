from tkinter import Menu

# default settings
TEXTURES = ['clip_art', 'hd']

class Settings:
    '''
    creates the top menu and assigns on-click commands
    '''
    def __init__(self, window, list_of_commands) -> None:
        self.window = window
        self.commands = list_of_commands

        # top menu
        self.mainmenu = Menu(self.window)

        # textures options
        textures_menu = Menu(self.mainmenu, tearoff=0)
        textures_menu.add_command(label='Clip Art', command=self.commands[0])
        textures_menu.add_command(label='HD', command=self.commands[1])

        # duplicates options
        self.duplicates_menu = Menu(self.mainmenu, tearoff=0)

        # add textures and duplicates options to top menu
        self.mainmenu.add_cascade(label='Textures', menu=textures_menu)
        #self.mainmenu.add_cascade(label='Allow duplicates', menu=self.duplicates_menu)