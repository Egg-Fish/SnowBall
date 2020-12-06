from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout

class Palette(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass

class Frame(Screen):
    def rail_open(self):
        if self.ids.rail.rail_state == "open":
            self.ids.rail.rail_state = "close"
        else:
            self.ids.rail.rail_state = "open"
    pass

class MultiFile1(MDBoxLayout):
    pass

class MultiFile2(MDBoxLayout):
    pass

Builder.load_file("kv/mf1.kv")

class testApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Dark"
        return Frame()

app = testApp()
app.run()
