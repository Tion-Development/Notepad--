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

def startgui(textInp):
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
                text = ''
            ))

            wf.add_widget(Button(
                text = 'Open',
                on_press = self.open,
                size_hint = (0.1, .04),
                pos = (0, 680)
            ))

            wf.add_widget(Button(
                text = 'Save',
                on_press = self.save,
                size_hint = (0.1, .04),
                pos = (150, 680)
            ))

            wf.add_widget(Button(
                text = 'New',
                on_press = self.new,
                size_hint = (0.1, .04),
                pos = (300, 680)
            ))

            self.root.add_widget(wf)

            
        def open(self, instance):
            # Меню выбора файла


            self.root.children[0].children[3].text = textInp
            # Нужно замещать текст, только если пользователь выбрал другой файл. Т.е. мне нужно возвращать пусть к выбранному файлу.

            # После равно нужнен результат ф-ции (там где '')

        def save(self, instance, textInp):
            text = self.root.children[0].children[3].text
            return text
            # В переменной text лежит твой текст
            
        def new(self, instance):
            self.root.children[0].children[3].text = ''
            # Cюда новый

        def on_start(self):
            th = threading.Thread(target= self.make_work_filed)
            th.start()


    Notepad().run()
