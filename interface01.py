from kivy.app import App
from kivy.uix.label import Label

def alomundo(texto):
    print (texto)

class FirstKivy(App):

    def build(self):
        return Label(text="Alô SEVIR!")

FirstKivy().run()