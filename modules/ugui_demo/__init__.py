from app import App
from scheduler import get_scheduler

import hardware_setup
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton
from gui.core.writer import CWriter
import gui.fonts.arial10 as arial10
from gui.core.colors import *

class BaseScreen(Screen):
    def __init__(self):

        def my_callback(button, arg):
            print('Button pressed', arg)
        
        super().__init__()
        wri = CWriter(ssd, arial10, GREEN, BLACK, verbose=True)
        
        col = 2
        row = 2
        Label(wri, row, col, 'Simple Demo')
        row = 50
        Button(wri, row, col, text='Yes', callback=my_callback, args=('Yes',))
        col += 60
        Button(wri, row, col, text='No', callback=my_callback, args=('No',))
        CloseButton(wri)

class uGUIDemo(App):

    def on_start(self):
        super().on_start()
        get_scheduler().set_sleep_enabled(False)
        Screen.change(BaseScreen)

    def on_activate(self):
        super().on_activate()

    def update(self):
        return

    def on_deactivate(self):
        return
