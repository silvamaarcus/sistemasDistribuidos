import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Temperatura: ", font_size=35))
        self.temperatura = TextInput(multiline=False, font_size=40, readonly=True,)
        self.inside.add_widget(self.temperatura)

        self.inside.add_widget(Label(text="Umidade: ", font_size=35))
        self.umidade = TextInput(multiline=False, font_size=40, readonly=True)
        self.inside.add_widget(self.umidade)

        self.add_widget(self.inside)
        self.submit = Button(text="Buscar", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        temperatura = self.temperatura.text
        umidade = self.umidade.text

        url = 'https://api.thingspeak.com/channels/1158494/feeds.json?api_key=ULRUYX5OKENDO6X7&results=2'
        r = requests.get(url)
        r = r.json()['feeds'][-1]

        self.temperatura.text = str(r['field2'] + "º")
        self.umidade.text = str(r['field2']) + "%"


class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()
