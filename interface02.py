from kivy.app import App
from kivy.uix.button import Button

def alomundo(texto):
    print (texto)

class FirstKivy(App):

    def build(self):

        return Button(text="Analise!", pos=(300, 350), size_hint=(.25, .18))

FirstKivy().run()