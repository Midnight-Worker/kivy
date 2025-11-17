# main.py
from kivy.app import App

class HelloApp(App):
    def say_hello(self):
        print("Button gedrückt")

HelloApp().run()
