import os, pickle, datetime, random
from main import JournalEntry, Journal, Snowball, SnowballContainer


f = "./SnowBall.p"

def saveData():
    with open(f, 'wb') as pf:
        pickle.dump(rawdata, pf)


try:
    with open(f, 'rb') as pf:
        rawdata = pickle.load(pf) 

except:
    print("Creating new data...")
    rawdata = {}
    rawdata["journal"] = Journal()
    rawdata["snowballcontainer"] = SnowballContainer()
    saveData()

def printData():
    
    print("Length of Journal:", len(rawdata["journal"]))
    print("IDs:", rawdata["journal"].getIDs())

    print("Length of Snowball Container:", len(rawdata["snowballcontainer"]))
    print("IDs:", rawdata["snowballcontainer"].getIDs())

    for entry in rawdata["journal"].entries:
        print("[JournalEntry]".center(50, '-'))
    
        print("Name:", entry.getName())
        print("Date", entry.getDate())
        print("Data:", entry.getData())
        print("Tag:", entry.getTag())
        print("ID:", entry.getID())
    

    print("--".center(50, '-') + "\n\n")


    for sb in rawdata["snowballcontainer"].snowballs:
        print("[Snowball]".center(50, '-'))

        print("Name:", sb.getName())
        print("Description:", sb.getDescription())
        print("Date:", sb.getDate())
        print("Frequency:", sb._frequency)
        print("Level:", sb.getLevel())
        print("Last Completed:", sb.getLastCompleted())
        print("Completions:", sb._n_completions)
        print("ID:", sb.getID())

    print("--".center(50, '-') + "\n\n")



def createDummyEntry():
    e = JournalEntry()
    e.setName(f"My {random.randint(100, 200)}nd egg adventure")
    e.setDate(datetime.datetime.today())
    e.setData("Today, I pooped like never before!")
    e.setTag("Green")
    e.setID(random.randint(1, 99999))

    rawdata["journal"] + e
    saveData()

def createDummySnowball():
    sb = Snowball()
    sb.setName(f"Eat {random.randint(2,10000)} Eggs")
    sb.setDescription("Just a test snowball ykyk")
    sb.setDate(datetime.datetime.today())
    sb.setFrequency(random.randint(1,7))
    sb.setID(random.randint(1, 99999))

    rawdata["snowballcontainer"] + sb
    saveData()

while True:
    print(
            "1. Dummy Entry\n"
            "2. Dummy Snowball\n"
            "3. Print Data\n"
        )


    opt = int(input("What would you like to do?: "))

    if opt == 0:
        break

    elif opt == 1:
        createDummyEntry()

    elif opt == 2:
        createDummySnowball()

    elif opt == 3:
        printData()

    elif opt == 4:
        rawdata["snowballcontainer"].snowballs[0].completedToday() # Local
