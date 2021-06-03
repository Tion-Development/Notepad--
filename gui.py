from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.image import Image
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

        def make_white(self):
            time.sleep(5.0)
            self.root.remove_widget(self.root.children[0])
            self.root.add_widget(Image(
                size = (1280, 720),
                pos = (0, 0),
                source = ''
            ))

        def on_start(self):
            th = threading.Thread(target= self.make_white)
            th.start()


    Notepad().run()

def returnText():
    text = "TEXT"
    return text

if __name__ == '__main__':
    startgui()