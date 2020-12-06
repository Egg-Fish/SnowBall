import os

os.chdir("SnowBall")

files = [
    '__main__.py',
    '__init__.py',
    'SnowBall.kv',
    'assets',
    'kv',
]

assets = [
    'penguin.png',
    'Snowball.png',
]

kvfiles = [
    'WelcomeScreen.kv',
    'JournalScreen.kv',
    'JournalEditScreen.kv',
    'JournalEntryScreen.kv',
    'SnowballScreen.kv',
    'SnowballEditScreen.kv',
    'SnowballEntryScreen.kv',
    'ReminderWidget.kv',
    'JournalEntryWidget.kv',
    'SnowballWidget.kv',
]

print("SnowBall".center(50,"-"))

for file in files:
    if file not in os.listdir('.'):
        print(f"ERROR: {file} not found in .")
    else:
        print(f"Loading ./{file}")

for asset in assets:
    if asset not in os.listdir('./assets'):
        print(f"ERROR: {asset} not found in ./assets")
    else:
        print(f"Loading ./assets/{asset}")

for kvfile in kvfiles:
    if kvfile not in os.listdir('./kv'):
        print(f"ERROR: {kvfile} not found in ./kv")
    else:
        print(f"Loading ./kv/{kvfile}")

print("Check Complete".center(50,"-"))
