from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text="Alô Sevir!"))
        self.add_widget(Button(text="Análise!"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class FirstKivy(App):

    def build(self):
        return MyGrid()

FirstKivy().run()