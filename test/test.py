from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

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

class testApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"
        return Frame()

app = testApp()
app.run()
