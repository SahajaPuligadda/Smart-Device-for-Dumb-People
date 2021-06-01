# creating a virtual keyboard
from datetime import datetime
from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from gtts import gTTS
import os


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.up_block = GridLayout()
        self.up_block.cols = 2

        # code for creating commonly used words btns
        self.com_words = GridLayout()
        self.com_words.cols = 1
        self.ok = Button(text="OK", font_size=30)
        self.ok.bind(on_press=self.pressed)
        self.com_words.add_widget(self.ok)

        self.hello = Button(text="Hello", font_size=20)
        self.hello.bind(on_press=self.press_btn)
        self.com_words.add_widget(self.hello)

        self.thankyou = Button(text="Thank You", font_size=20)
        self.thankyou.bind(on_press=self.press_btn)
        self.com_words.add_widget(self.thankyou)

        self.bye = Button(text="Bye", font_size=20)
        self.bye.bind(on_press=self.press_btn)
        self.com_words.add_widget(self.bye)

        self.sorry = Button(text="Sorry", font_size=20)
        self.sorry.bind(on_press=self.press_btn)
        self.com_words.add_widget(self.sorry)

        self.help = Button(text="I need HELP", font_size=20)
        self.help.bind(on_press=self.press_btn)
        self.com_words.add_widget(self.help)

        self.water = Button(text="Please give me a glass of water", font_size=20)
        self.water.bind(on_press=self.press_btn)
        self.com_words.add_widget(self.water)

        self.up_block.add_widget(self.com_words)

        # text box creation code
        self.name = TextInput(multiline=True)
        self.up_block.add_widget(self.name)

        self.add_widget(self.up_block)

    def pressed(self, instance):
        txt = self.name.text
        print(txt)
        language = 'en'
        # converting text to speech
        output = gTTS(text=txt, lang=language, slow=False)
        date_string = datetime.now().strftime("%d%m%Y%H%M%S")
        filename = "voice" + date_string + ".mp3"
        output.save(filename)
        os.system("start " + filename)

    def press_btn(self, instance):
        txt = ''
        if instance == self.thankyou:
            txt = self.thankyou.text
        elif instance == self.hello:
            txt = self.hello.text
        elif instance == self.bye:
            txt = self.bye.text
        elif instance == self.sorry:
            txt = self.sorry.text
        elif instance == self.help:
            txt = self.help.text
        elif instance == self.water:
            txt = self.water.text
        print(txt)
        language = 'en'
        # converting text to speech
        output = gTTS(text=txt, lang=language, slow=False)
        date_string = datetime.now().strftime("%d%m%Y%H%M%S")
        filename = "voice" + date_string + ".mp3"
        output.save(filename)
        os.system("start "+filename)


class MyNotepad(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    Config.set('kivy', 'keyboard_mode', 'systemanddock')
    MyNotepad().run()
