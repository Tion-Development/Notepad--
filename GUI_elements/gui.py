from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

import os
import time 
import threading

def startgui():
    class Notepad(App):
        def build(self):
            
            Config.set('graphics', 'width', 1280)
            Config.set('graphics', 'height', 720)
            Config.write()

            main = FloatLayout(size = (1280, 720))

            main.add_widget(Image(
                size = (1280, 720),
                pos = (0, 0),
                source = os.getcwd()+'\\img\\bg.jpg'
            ))

            return(main)

        def make_work_filed(self):
            time.sleep(3.0)
            self.root.remove_widget(self.root.children[0])
            
            wf = FloatLayout(size = (1280, 720))

            wf.add_widget(Image(
                pos = (0,0),
                size = (1280, 720)
            ))

            wf.add_widget(TextInput(
                multiline = True,
                size_hint = (1, .95),
                pos = (0,0),
                background_color = (256, 256, 256, 0),
                text = 'Сюда Вы можете писать свой текст'
            ))


            self.root.add_widget(wf)

            
        def on_start(self):
            th = threading.Thread(target= self.make_work_filed)
            th.start()


    Notepad().run()

def returnText():
    text = "TEXT"
    return text

if __name__ == '__main__':
    startgui()