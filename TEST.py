from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.update)

        return button
    
    def update(self,event):
        self.button.text = 'Hello to Kivy'

if __name__ == '__main__':
    app = MainApp()
    app.run()
