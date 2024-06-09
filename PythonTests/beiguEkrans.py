from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.core.window import Window
import os
from kivy.uix.image import Image

Window.size = (400, 400)
Window.clearcolor = (110/255, 55/255, 110/255, 1)
Window.title = "Python tests - Rezultāti"

class Rezultats(App):
    punkti = NumericProperty(0)

    def __init__(self, punkti, **kwargs):
        super().__init__(**kwargs)
        self.punkti = punkti

    def clear_points(self, instance):
        self.punkti = 0
        self.stop()

    def build(self):
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        if self.punkti <= 3:
            image_path = source=os.path.join(os.path.dirname(__file__), 'images/minimun.png'),
            message = 'Varēji arī labāk!'
        elif self.punkti > 3 and self.punkti <= 6:
            image_path = source=os.path.join(os.path.dirname(__file__), 'images/medium.png'), 
            message = 'Labs rezultāts!'
        else:
            image_path = source=os.path.join(os.path.dirname(__file__), 'images/maximum.png'), 
            message = "Malacis!"

        result_image = Image(
            source=image_path,
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5}
        )
        
        final_label = Label(
            text=f'Paldies par piedalīšanos testā!\n Tavs rezultāts: {self.punkti} atbildes no pirmās reizes.\n{message}',
            font_size='20sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.5)
        )
        final_label.bind(size=final_label.setter('text_size'))

        clear_button = Button(
            text='Apturēt',
            size_hint=(0.5, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        clear_button.bind(on_press=self.clear_points)

        box.add_widget(final_label)
        box.add_widget(result_image)
        box.add_widget(clear_button)
        
        return box
