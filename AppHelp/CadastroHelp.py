from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

class Login(App):

    def build(self):
        layout = FloatLayout()

        text1 = Label(text='Email', size_hint = (0.2, 0.1), pos_hint = {'center_x':0.33 , 'center_y': 0.7})
        
        caixa1 = TextInput(hint_text='Digite o seu Email...', size_hint = (0.4, 0.05), pos_hint={'center_x':0.5, 'center_y':0.65})
        
        text2 = Label(text='Senha', size_hint = (0.2, 0.1), pos_hint = {'center_x': 0.33, 'center_y': 0.6})

        caixa2 = TextInput(hint_text='Digite sua Senha...', password=True, size_hint = (0.4, 0.05), pos_hint = {'center_x': 0.5, 'center_y': 0.55})  

        botao1 = Button(text='Entrar', size_hint = (0.09, 0.08), pos_hint = {'center_x':0.655, 'center_y':0.43}, background_color = ('0B4DC7'))


        layout.add_widget(text1)
        layout.add_widget(caixa1)
        layout.add_widget(text2)
        layout.add_widget(caixa2)
        layout.add_widget(botao1)

        return layout


Window.clearcolor = 'green'
Window.size = (600, 600)

# Run the application
Login().run()