from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDDatePicker

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.clock import Clock

import datetime
import pickle
import random



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



class JournalEntryWidget(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__()
        self._journal_entry = kwargs["journal_entry"]
        
        self.ids.tagImage.md_bg_color = SnowBall.COLORS[self._journal_entry.getTag()] 
        self.ids.Name.text = self._journal_entry.getName()
        self.ids.SecondaryText.text = self._journal_entry.getDate().date().isoformat()


class SnowballWidget(MDBoxLayout):
    pass


class TagRow(MDBoxLayout):
    def setCurrent(self, tag):
        self.parent.parent.parent.parent.journal_entry._tag = tag
    pass

class Tag(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self._color = kwargs["tagColor"]
        self.background_color = SnowBall.COLORS[self._color] 
        self.event = Clock.schedule_interval(self.updateCurrentStatus, 0.1) 

    def _updateCurrent(self, tag):
        self.parent.setCurrent(tag)
    
    def updateCurrentStatus(self, _):
        try:
            if self.parent.parent.parent.parent.parent.journal_entry._tag == self._color:
                self.size_hint = (1, 0.6)
            else:
                self.size_hint = (1, 0.2)
        except:
            self.event.cancel()





class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class JournalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._journal = Journal()        
        self._journal_entry_widgets = []
        self.bind(on_pre_enter=self._preEnter)
         
        self._range = []


    def _preEnter(self, _):
        self.ids.entries.bind(minimum_height=self.ids.entries.setter('height'))
        self._range = []
        self._journal_entry_widgets = []
        self._journal = SnowBall.getJournal()
        self.ids.entries.clear_widgets()
        self._createJournalEntryWidgets()

    def _pickFilterRange(self):
        self._range = []
        picker = MDDatePicker(callback=self._setStartDate)
        picker.open()


    def _setStartDate(self, time):
        self._range.append(time)

        picker = MDDatePicker(callback=self._setEndDate, min_date = time)
        picker.open()

    def _setEndDate(self, time):
        self._range.append(time)
        self._createJournalEntryWidgets()

    def _filterEntries(self):
        filtered = []

        for entry in self._journal.entries:
            if entry.getDate().date() >= self._range[0] and entry.getDate().date() <= self._range[1]:
                filtered.append(entry)

        return filtered
    
    def _displayEntries(self):
        self.ids.entries.clear_widgets() 
        for entry in reversed(self._journal_entry_widgets):
            self.ids.entries.add_widget(entry)


    def _createJournalEntryWidgets(self):
        if len(self._range) != 0:
            entries = self._filterEntries()
        
        else:
            entries = self._journal.entries

        self._journal_entry_widgets = []
        for entry in entries:
            widget = JournalEntryWidget(journal_entry=entry)
            self._journal_entry_widgets.append(widget)
            
        self._displayEntries()

    def _openJournalEditScreen(self, entry):
        self.manager._journal_entry_edit = entry
        self.manager.current = "JournalEditScreen"

class JournalEditScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_pre_enter=self.preEnter)

    def preEnter(self, _):
        print(self.manager._journal_entry_edit.getName())

class JournalEntryScreen(Screen):
    tc = ListProperty((1,1,1,0))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.journal_entry = JournalEntry()
        self.journal_entry.setTag("Blue")
        self.bind(on_pre_enter=self.preEnter) 
        

    def preEnter(self, _):
        self.ids.tagrow.clear_widgets()

        for color in SnowBall.COLORS:
            print(color)
    
            self.ids.tagrow.add_widget(Tag(tagColor=color, id=color))
    
        Clock.schedule_interval(self.updateColor, 0.01)

    def updateColor(self, _):
        self.tc = SnowBall.COLORS[self.journal_entry.getTag()]

    def createJournalEntry(self):
        self.journal_entry.setName(self.ids.name.text)
        self.journal_entry.setData(self.ids.data.text)
        self.journal_entry.setDate(datetime.datetime.today())

        SnowBall.addJournalEntry(self.journal_entry)
        self.manager.current = "WelcomeScreen"
        
        self.ids.name.text = ""
        self.ids.data.text = ""
        self.journal_entry = JournalEntry()
        self.journal_entry.setTag("Blue")

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





class SnowBallApp(MDApp):
    rawdata = None
    def _getData(self):
        with open(self._data_file_path, "rb") as pf:
            self.rawdata = pickle.load(pf)
    
    def _saveData(self):
        with open(self._data_file_path, "wb+") as pf:
            pickle.dump(self.rawdata, pf)


    def debugInfo(self):
        print('[DEBUGINFO]'.center(80, '-'))

        print("Length of Journal:", len(self._journal))
        print("IDs:", self._journal.getIDs())
        print("Length of Snowball Container:", len(self._snowballcontainer))
        print("IDs:", self._snowballcontainer.getIDs())


        for entry in self._journal.entries:
            print('[ENTRY]'.center(80, '-'))
            print("Name:", entry.getName())
            print("Date:", entry.getDate())
            print("Tag:", entry.getTag())
            print("ID:", entry.getID())
            print("\nData:", entry.getData())

        print('--'.center(80, '-'))

        for sb in self._snowballcontainer.snowballs:
            print("[SNOWBALL]".center(80, '-'))

            print("Name:", sb.getName())
            print("Date Created:", sb.getDate())
            print("Description:", sb.getDescription())
            print("Frequency: Every " + str(sb._frequency) + " days")
            print("Level:", sb.getLevel())
            print("Last Completed:", sb.getLastCompleted())
            print("Completions:", sb._n_completions)
            print("\nID:", sb.getID())

        print('--'.center(80, '-'))
        
    def build(self):
        Builder.load_file('MainLayout.kv')
        self.COLORS = {"Red": (1,0,0,1), "Green": (0,1,0,1), "Blue":(0,0,1,1), "Yellow": (1,1,0,1), "Purple": (1,0,1,1)}
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"
        
        self._data_file_path = "SnowBall.p"

        try:
            self._getData()
        except:
            self.rawdata = {"journal": Journal(), "snowballcontainer": SnowballContainer()}
            self._saveData()

        self._journal = self.rawdata["journal"]
        self._snowballcontainer = self.rawdata["snowballcontainer"]
        return MainLayout() 

    def addJournalEntry(self, entry):
        ID = random.randint(0, 99999999)

        if ID in self._journal.getIDs():
            ID = random.randint(0, 99999999)

        entry.setID(ID)
        self._journal + entry
        self._saveData()
        
    def updateJournalEntry(self, entry):
        self._journal * entry
        self._saveData()

    def removeJournalEntry(self, entry):
        self._journal - entry
        self._saveData()

    
    def getJournal(self):
        return self._journal

    def getSnowballs(self):
        return self._snowballcontainer.snowballs

    
if __name__ == "__main__":
    SnowBall = SnowBallApp()
    SnowBall.run()
    
