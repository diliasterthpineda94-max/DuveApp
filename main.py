from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import QLabel
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class EmotionalAssistentApp(App):
  def build(self):
    # pantalla principal vertical
    layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
    # Titulo de la app
    title_label = QLabel(
        text='Tu Asistente Emocional',
        font_size=22,
        size_hint_y=None.
        height=50,
        halign='center'
        valign='middle'
    )
    layout.add_widget(title_label)

    # Area de chat / conversacion (usamos Scrollview para que no se desborde)
    self.chat_history = QLabel(
        text='Hola Duveir. ¿Como te sientes hoy? Cuentame lo que quieras, aquib estoy para escucharte.',
        font_size=16,
        halign='left'
        valign='top'
    )
    self.chat_history.bind(size=self.chat_history.setter('text_size'))

    scroll = Scrollview(size_hint=(1, 1))
    scroll.add_widget(self.chat_history)
    layout.add_widget(scroll)

    # Caja de texto para escribir el mensaje
    self.user_input = TextIput(
        text='',
        hint_text='Escribe aqui como te sientes...',
        size_hint_y=None,
        height=50,
        multiline=False
    )
    layout.add_widget(self.user_input)

    # Boton de enviar
    send_button = Button(
        text='Enviar',
        size_hint_y=None,
        height=50,
        background_color=(0.1, 0.5, 0.8, 1)
    )
    send_button.bind(on_press=self.send_message)
    layout.add_widget(send_button)

    return layout

    def send_message(self, instance):
      mensaje =self.user_input.text.strip()
      if mensaje:
        # Respuesta sencilla de apoyo emocional por ahora
        respuesta = f"\nTu: {mensaje}\nAsistente: Te entiendo perfectamente. Estoy aqui acompañandote en este momento. Respira profundo, todo va a estar bien. \n"
        self.chat_history.text += respuesta
        self.user_input.text =''


if __name__ == '__main__':
  EmotionalAsistantApp().run()
