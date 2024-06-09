from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.image import Image
import os
from jautajums1 import Jautajums_1

Window.size = (400, 400)
Window.clearcolor = (110/255, 55/255, 110/255, 1)
Window.title = "Python tests"

class Tests(App):
    punkti = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sakums = Label(
            text='Laipni lūdzam testā!\nJums jāatbild uz 10 jautājumiem.\nTiks doti 4 atbilžu varianti, no kuriem tikai 2 ir pareizi.',
            font_size='20sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.5)
        )
        self.sakums.bind(size=self.sakums.setter('text_size'))
        
        self.poga = Button(
            text='Sākt testēšanu',
            size_hint=(0.5, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        self.poga.bind(on_press=self.open_question_screen)

        
    def build(self):
        sakumaImage = Image(
            source=os.path.join(os.path.dirname(__file__), 'images/sillyCar.png'),
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5}
        )

        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        top = Widget(size_hint_y=None, height=50)
        box.add_widget(top)
        box.add_widget(self.sakums)
        
        mid = Widget(size_hint_y=None, height=25)
        box.add_widget(sakumaImage)
        box.add_widget(mid)
        box.add_widget(self.poga)

        self.poga.background_color = (120/255, 10/255, 120/255, 1)
        return box

    def open_question_screen(self, instance):
        self.stop()
        Jautajums_1(punkti=self.punkti).run()

if __name__ == "__main__":
    Tests().run()