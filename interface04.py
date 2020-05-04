from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import fundamentus

TABELA = fundamentus.get_data()

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="TICK da Empresa: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.add_widget(self.inside)

        self.submit = Button(text="Buscar dados", font_size=30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.tick = Label(text="Resultado!")
        self.add_widget(self.tick)

    def pressed(self, instance):
        tick = self.name.text
        self.tick.text = "P/L da ação " + tick + " = " + str(TABELA[tick]['P/L'])
        self.name.text = ""

class FirstKivy(App):

    def build(self):
        return MyGrid()

FirstKivy().run()