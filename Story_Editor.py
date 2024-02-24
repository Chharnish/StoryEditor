"""
main() - of course.
Runs the main loop
Calls a menu
Sends control to other parts of the program

getMenuChoice()
prints a menu of user options
repeats if input is invalid
returns a valid menu choice

playGame()
plays the game
Keeps going until next node is "quit"

playNode()
given the game data and a node,
plays out the node
returns the next node

getDefaultGame()
creates a single-node default game
returns that data structure

editNode()
given the current game structure...
list all the current node names
get a node name
if that node exists
copy that node to newNode
otherwise...
create newNode with empty data
use editField() to allow user to edit each node
return the now edited newNode

editField()
get a field name
print the field's current value
if the user presses 'enter' immediately
retain the current value
otherwise...
use the new value

saveGame()
save the game to a data file
you can preset the file name (eg 'game.dat')
print the current game dictionary in human-readable format
Save the file in JSON format

loadGame()
presume there is a data file named 'game.dat' in the current directory
open that file
load the data into the game object
return that game object



Coded by yours truly, 
Jeremy Escobar - hater of sandwiches
Saa Weathers
Brian Kelly

"""


import json

def getMenuChoice():
    keepGoing = True
    while keepGoing:
        print("""
    0) exit
    1) load default game
    2) load game file
    3) save current game file
    4) edit or add a node
    5) play current game file
    """)

        menuChoice = input("Please input your choice: ")
        if menuChoice in ("0", "1","2","3","4","5"):
            keepGoing = False
        else: 
            print("that is not a valid choice")

    return menuChoice 

def getDefaultGame():
    GAME = {
        "start" : ["This is a default game", "Play again?", "start", "Quit to main menu", "quit"]
    }

    print("Default game loaded successfully")
    
    return GAME



def playGame(GAME): 
    node = "start"
    keepGoing = True
    if node in GAME.keys():
        while keepGoing:
            node = playNode(GAME,node)
            if node == "quit":
                keepGoing = False


def playNode(GAME,node):
    print(f"""
        {GAME[node][0]}
        1) {GAME[node][1]}
        2) {GAME[node][3]}
""")
    choice = input("Please choose an option: ")
    if choice == "1":
        node = GAME[node][2]
    elif choice == "2":
        node = GAME[node][4]
    else:
        print("that choice is not a valid option")
    return node

def saveGame(GAME):
    if GAME != None:
        outFile = open("GAME.json", "w")
        json.dump(GAME, outFile, indent=2)
        outFile.close()
        for node in GAME:
            print(node, ":", GAME[node])
        print("Saving...")
    else:
        print("No game data to save!")

def loadGame():
    outFile = open("GAME.json", "r")
    GAME = json.load(outFile)
    outFile.close()
    print("loading file...")
    for node in GAME:
            print(node, ":", GAME[node])
    return GAME

def editNode(GAME):
    nodeNames = GAME.keys()
    for nodeName in nodeNames:
        print(nodeName)

    newName = input("Please input new node name or existing node to edit: ")
    if newName in nodeNames:
        newNode = GAME[newName]
        print("editing node...")

    else: 
        newNode = ("", "", "", "", "")
        print("creating node...")


    (desc, nodeA, goToA, nodeB, goToB) = newNode

    newDesc =  editField("description", desc)
    newnodeA = editField("option 1", nodeA)
    newgoToA = editField("destination 1", goToA)
    newnodeB = editField("option 2", nodeB)
    newgoToB = editField("destination 2", goToB)

    newNode = (newDesc, newnodeA, newgoToA, newnodeB, newgoToB)

    GAME[newName] = newNode

    return GAME
    

def editField(prompt, nodeGuts):
    test = input(f"Please input the new {prompt} ({nodeGuts}): ")
    return test
    


def main():
    GAME = None
    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            print("exiting...")
            keepGoing = False
        elif menuChoice == "1":
            GAME = getDefaultGame()
        elif menuChoice == "2":
            GAME = loadGame()
        elif menuChoice == "3":
            saveGame(GAME)
        elif menuChoice == "4":
            if GAME != None:
                editNode(GAME)
            else: 
                print("No game file selected!")
        elif menuChoice == "5":
            if GAME != None:
                playGame(GAME)
            else:
                print("No game file selected!")
        else:
            print("That was not a valid option")

main()