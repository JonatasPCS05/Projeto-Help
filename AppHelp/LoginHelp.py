from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

class Cadastro(App):
    def build(self):
        layout = FloatLayout()
        
        nome = Label(text = 'Nome', size_hint = (0.2, 0.2), pos_hint = {'center_x': 0.295, 'center_y':0.8})
        caixa_nome = TextInput(hint_text = 'Digite o seu Nome...', size_hint = (0.359, 0.051), pos_hint = {'center_x':0.44, 'center_y':0.75})
        email = Label(text = 'Email', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.295, 'center_y': 0.7})
        caixa_email = TextInput(hint_text = 'Digite o seu Email...', size_hint = (0.359, 0.051), pos_hint = {'center_x':0.44 , 'center_y': 0.65})
        confirmar_email = Label(text = 'Confirmar Email', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.350, 'center_y':0.6})
        caixa_confirmar_email = TextInput(hint_text = 'Confirme o seu Email...', size_hint = (0.359, 0.051), pos_hint = {'center_x':0.44,'center_y':0.55})
        senha = Label(text = 'Senha', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.295, 'center_y': 0.5})
        caixa_senha = TextInput(hint_text = 'Crie uma Senha...', password = True, size_hint = (0.359, 0.051), pos_hint = {'center_x':0.44, 'center_y':0.45})
        confirmar_senha = Label(text = 'Confirmar Senha', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.355, 'center_y':0.4})
        caixa_confirmar_senha = TextInput(hint_text = 'Confirme sua Senha...', password = True, size_hint = (0.359, 0.051), pos_hint = {'center_x':0.44, 'center_y':0.35})
        botao = Button(text='Cadastrar', size_hint = (0.14, 0.06), pos_hint = {'center_x':0.55, 'center_y':0.24}, background_color = ('0B4DC7'))
        
        layout.add_widget(nome)
        layout.add_widget(caixa_nome)
        layout.add_widget(email)
        layout.add_widget(caixa_email)
        layout.add_widget(confirmar_email)
        layout.add_widget(caixa_confirmar_email)
        layout.add_widget(senha)
        layout.add_widget(caixa_senha)
        layout.add_widget(confirmar_senha)
        layout.add_widget(caixa_confirmar_senha)
        layout.add_widget(botao)
        return layout
    Window.clearcolor = 'green'
    Window.size = (600, 600)
Cadastro().run()

