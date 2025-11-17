# main.py
from kivy.app import App
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        btn = Button(text="Hallo")
        btn.bind(on_press=self.button_pressed)
        return btn

    def button_pressed(self, instance):
        print("Button gedrückt")

HelloApp().run()