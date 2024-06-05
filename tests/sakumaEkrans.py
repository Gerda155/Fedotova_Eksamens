from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty
from jautajums1 import *

# Глобальные настройки
Window.size = (400, 300)
Window.clearcolor = (209/255, 130/255, 210/255, 1)
Window.title = "Python tests"

class MainScreen(App):
    punkti = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sakums = Label(
            text='Laipni lūdzam testā!\nJums jāatbild uz 10 jautājumiem.\nJums tiks doti 4 atbilžu varianti, no kuriem tikai 2 ir pareizi.',
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
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        top_spacer = Widget(size_hint_y=None, height=50)
        box.add_widget(top_spacer)
        box.add_widget(self.sakums)
        
        mid_spacer = Widget(size_hint_y=None, height=50)
        box.add_widget(mid_spacer)
        box.add_widget(self.poga)
        return box

    def open_question_screen(self, instance):
        self.stop()
        QuestionScreen(punkti=self.punkti).run()

if __name__ == "__main__":
    MainScreen().run()
