from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import datetime




class JournalEntry():
    def __init__(self):
        self._name = ""
        self._date = None
        self._data = ""
        self._tag = ""
        self._id = 0

    def getName(self):
        return self._name

    def getDate(self):
        return self._date

    def getData(self):
        return self._data

    def getTag(self):
        return self._tag

    def getID(self):
        return self._id

    def getMonth(self):
        return self._date.month

    def getYear(self):
        return self._date.year

    def setName(self, name):
        self._name = name

    def setDate(self, dt):
        self._date = dt

    def setData(self, data):
        self._data = data

    def setTag(self, tag):
        self._tag = tag

    def setID(self, ID):
        self._id = ID
        

class Journal():
    def __init__(self):
        self._date = datetime.datetime.today()
        self.entries = []

    def __len__(self):
        return len(self.entries)

    def __add__(self, entry):
        self.entries.append(entry)

    def __sub__(self, entry):
        entry_id = entry.getID()
        pop_index = 0

        for i in range(len(self.entries)):
            if self.entries[i].getID() == entry_id:
                pop_index = i
                break

        self.entries.pop(pop_index)

    def __mul__(self, entry):
        entry_id = entry.getID()
        edit_index = 0

        for i in range(len(self.entries)):
            if self.entries[i].getID() == entry_id:
                edit_index = i
                break

        self.entries[edit_index].setName(entry.getName())
        self.entries[edit_index].setDate(entry.getDate())
        self.entries[edit_index].setData(entry.getData())
        self.entries[edit_index].setTag(entry.getTag())
    
    def getIDs(self):
        ids = [x.getID() for x in self.entries]
        return ids







class Snowball():
    def __init__(self):
        self._name = ""
        self._description = ""
        self._frequency = 0
        self._level = 0
        self._id = 0
        self._date = None
        self._n_completions = 0
        self._last_completed = None
        self._tolerance = 3
    
    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getDate(self):
        return self._date

    def getLevel(self):
        return self._level

    def getID(self):
        return self._id

    def updateLevel(self):
        if (self._date != None and self._frequency != 0):
            if self._n_completions >= 7:
                self._level = 1
            if self._n_completions >= 14:
                self._level = 2
            if self._n_completions >= 21:
                self_level = 3
            
            tol_delta = datetime.timedelta(days=self._frequency+self._tolerance)
            cutoff_date = self._last_completed + tol_delta

            if datetime.datetime.today() > cutoff_date:
                self._n_completions = 0

    def getLastCompleted(self):
        return self._last_completed
    
    def setName(self, name):
        self._name = name

    def setDescription(self, desc):
        self._description = desc

    def setFrequency(self, freq):
        self._frequency = freq

    def setID(self, ID):
        self._id = ID

    def setDate(self, dt):
        self._date = dt

    def completedToday(self):
        self._last_completed = datetime.datetime.today()
        self.updateLevel()
        self._n_completions += 1
    
class SnowballContainer():
    def __init__(self):
        self.snowballs = []

    def __len__(self):
        return len(self.snowballs)

    def __add__(self, snowball):
        self.snowballs.append(snowball)

    def __sub__(self, snowball):
        snowball_id = snowball.getID()
        pop_index = 0

        for i in range(len(self.snowballs)):
            if self.snowballs[i].getID() == snowball_id:
                pop_index = i
                break

        self.snowballs.pop(pop_index)

    def __mul__(self, snowball):
        snowball_id = snowball.getID()
        edit_index = 0

        for i in range(len(self.snowballs)):
            if self.snowballs[i].getID() == snowball_id:
                edit_index = i
                break

        self.snowballs[edit_index].setName(snowball.getName())
        self.snowballs[edit_index].setFrequency(snowball.getFrequency())
        self.snowballs[edit_index].setDescription(snowball.getDescription)
    

    def getIDs(self):
        ids = [x.getID() for x in self.snowballs]
        return ids



class ReminderWidget(MDBoxLayout):
    pass

class JournalEntryWidget(MDBoxLayout):
    pass

class SnowballWidget(MDBoxLayout):
    pass




class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._reminders = []
        self._reminder_widgets = []

        self._reminders = self._getReminders()
        

    def _getReminders(self):
        pass

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
        self.journal_entry_edit = None
        self.snowball_edit = None
        



class MainLayout(MDBoxLayout):
    pass




Builder.load_file('SnowBall.kv')
Builder.load_file('kv/JournalScreen.kv')
Builder.load_file('kv/WelcomeScreen.kv')
Builder.load_file('kv/JournalEditScreen.kv')
Builder.load_file('kv/JournalEntryScreen.kv')
Builder.load_file('kv/SnowballScreen.kv')
Builder.load_file('kv/SnowballEditScreen.kv')
Builder.load_file('kv/SnowballEntryScreen.kv')
Builder.load_file('kv/ReminderWidget.kv')
Builder.load_file('kv/JournalEntryWidget.kv')
Builder.load_file('kv/SnowballWidget.kv')




class SnowBallApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"
        return MainLayout()
    
    

if __name__ == '__main__':
    SnowBall = SnowBallApp()
    SnowBall.run()
