from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import datetime




class JournalEntry():
    pass

class Journal():
    pass

class Snowball():
    pass

class SnowballContainer():
    pass




class ReminderWidget(MDBoxLayout):
    pass

class JournalEntryWidget(MDBoxLayout):
    pass

class SnowballWidget(MDBoxLayout):
    pass




class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class JournalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class JournalEditScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class JournalEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SnowballScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SnowballEditScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SnowballEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




class Screens(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




class MainLayout(MDBoxLayout):
    pass




class SnowBallApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"
        return MainLayout()


if __name__ == '__main__':
    app = SnowBallApp()
    app.run()
