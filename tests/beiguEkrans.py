from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty

class FinalScreen(App):
    punkti = NumericProperty(0)

    def __init__(self, punkti, **kwargs):
        super().__init__(**kwargs)
        self.punkti = punkti

    def clear_points(self):
        self.punkti = 0
        self.stop()

    def build(self):
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.final_label = Label(
            text=f'Paldies par piedalīšanos testā!\n Tavs rezultāts: {self.punkti} atbildes no pirmās reizes.',
            font_size='20sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.5)
        )
        self.final_label.bind(size=self.final_label.setter('text_size'))
        
        clear_button = Button(
            text='Apturēt',
            size_hint=(0.5, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        clear_button.bind(on_press=self.clear_points)
        
        box.add_widget(self.final_label)
        box.add_widget(clear_button)
        return box