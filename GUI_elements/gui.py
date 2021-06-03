from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.image import Image
import os

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
                source = '  '
            ))

    Notepad().run()

def returnText():
    text = "TEXT"
    return text

if __name__ == '__main__':
    startgui()