from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty
from jautajums7 import QuestionScreen7

# Глобальные настройки
Window.size = (400, 300)
Window.clearcolor = (209/255, 130/255, 210/255, 1)
Window.title = "Python tests - Question"

class QuestionScreen6(App):
    punkti = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.punkti = kwargs.get('punkti', 0)

    def __init__(self, punkti, **kwargs):
        super().__init__(**kwargs)
        self.punkti = punkti
        self.question = Label(
            text='6. jaut?',
            font_size='20sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.5)
        )
        self.question.bind(size=self.question.setter('text_size'))
        
        self.checkbox1, self.checkbox1_layout = self.create_checkbox('Atbilde 1')
        self.checkbox2, self.checkbox2_layout = self.create_checkbox('Atbilde 2')
        self.checkbox3, self.checkbox3_layout = self.create_checkbox('Atbilde 3')
        self.checkbox4, self.checkbox4_layout = self.create_checkbox('Atbilde 4')
        
        self.submit_btn = Button(
            text='Iesniegt',
            size_hint=(0.5, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        self.submit_btn.bind(on_press=self.submit_answer)
        
        self.error_label = Label(
            text='',
            color=(1, 0, 0, 1),
            font_size='16sp',
            size_hint=(1, None),
            height=30
        )
        
    def create_checkbox(self, text):
        layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
        checkbox = CheckBox()
        label = Label(text=text, size_hint=(1, None), height=40)
        layout.add_widget(checkbox)
        layout.add_widget(label)
        return checkbox, layout
    
    def build(self):
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        top_spacer = Widget(size_hint_y=None, height=20)
        box.add_widget(top_spacer)
        box.add_widget(self.question)
        
        box.add_widget(self.checkbox1_layout)
        box.add_widget(self.checkbox2_layout)
        box.add_widget(self.checkbox3_layout)
        box.add_widget(self.checkbox4_layout)
        
        mid_spacer = Widget(size_hint_y=None, height=20)
        box.add_widget(mid_spacer)
        box.add_widget(self.submit_btn)
        box.add_widget(self.error_label)
        return box

    def submit_answer(self, instance):
        is_correct = self.checkbox1.active and self.checkbox2.active and not self.checkbox3.active and not self.checkbox4.active
        
        if is_correct:
            self.punkti += 1
            self.stop()
            QuestionScreen7(punkti=self.punkti).run()
        else:
            self.error_label.text = 'Nepareiza atbilde, lūdzu mēģiniet vēlreiz.'
            self.clear_checkboxes()

    def clear_checkboxes(self):
        self.checkbox1.active = False
        self.checkbox2.active = False
        self.checkbox3.active = False
        self.checkbox4.active = False

if __name__ == "__main__":
    QuestionScreen6(punkti=0).run()
