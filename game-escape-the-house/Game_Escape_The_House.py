# ESCAPE THE HOUSE - GAME BY JOHNATHON A. KWISSES

""" This is a simple game made up of 7 different rooms and two outcomes;
win/lose.

The player starts in room 1 with a couple options presented to them. Each
option leads the player to different parts of
a house. The player has an inventory and can call items from it via
'inventory' or 'i'.

OBJECTIVE: Get out of the house alive.


Programmers Notes: 2 classes: MainMenu, InventoryItems. 7 main functions;
room_1() - room_7().
                   Inventory displayed and can be called at all main room
                   areas.
                   Console display should be 10 lines horizontal as this is
                   the format the game was coded in."""
# room_5() next

# ---------------------------------------------------------------------------------------------------------------------

# global lists
""" The lists are global as it produces less lines of code than a argument
instance. I am not worried about security
so this seemed to be the logical answer. (Try to avoid this way of
programming in the future """

inventory = ['key']
notebook_entries = []
open_door = []


# Main Menu


class MainMenu:
    """ Brings up the main menu for the game. The player has 3 options;
    start, instructions, and about.
    Start          initiates room_1()
    Instructions   prints the instructions for the game
    About          prints the about from another file """

    def __init__(self):
        pass

    def main_menu(self):
        self.__init__()
        print(
            "\nESCAPE THE HOUSE - MAIN "
            "MENU\n---------------------------------------")
        print("Start             1\nInstructions      2\nAbout             3")
        print("---------------------------------------\n")
        menu_choice = input("Enter number: ")
        if menu_choice == "1":
            room_1()
        elif menu_choice == "2":
            MainMenu.instructions()
        elif menu_choice == "3":
            MainMenu.about()
        else:
            MainMenu.main_menu()

    def instructions(self):
        self.__init__()
        print(
            "\nEscape The House features many different ways to interact "
            "with the game.\nThe player "
            "encounters different obstacles and has many different choices "
            "to make.\nAt any prompt when in a room, "
            "the user can type 'inventory' or 'i' to use items in their "
            "inventory.\nEg. notebook brings up a menu to "
            "either write/read in the item.\nOther items give just the "
            "description of the chosen item.\nGood Luck!\n")
        instructions_choice = input("Press Enter to continue: ")
        if instructions_choice == "":
            MainMenu.main_menu()
        else:
            MainMenu.main_menu()

    def about(self):
        self.__init__()
        f = open(
            "C:/Users/John/PycharmProjects/Personal "
            "Projects/Games/Game_Escape_The_House/about.txt",
            "r")
        print(f.read())
        about_choice = input("\nPress Enter to continue: ")
        if about_choice == "":
            MainMenu.main_menu()
        else:
            MainMenu.main_menu()


# Inventory Management


class InventoryItems:
    """ This class takes care of all item instances including the item calls
    and item properties. The class is called
    when a player input 'inventory' or 'i' on one of the main room screens. """

    def __init__(self):
        pass

    def inventory_call(self):
        self.__init__()
        inventory_item_call = input(
            "\n\nInventory: %s\n\n\n\n\n\nEnter item in inventory to use: "
            % inventory)
        if inventory_item_call == "notebook":
            if "notebook" in inventory:
                InventoryItems.item_notebook(self)
            else:
                print(
                    "\n\n'%s' not in inventory.\n\n\n\n\n" %
                    inventory_item_call)
                input("Press Enter to continue: ")
        elif inventory_item_call == "crowbar":
            if "crowbar" in inventory:
                InventoryItems().item_crowbar()
            else:
                print(
                    "\n\n'%s' not in inventory.\n\n\n\n\n" %
                    inventory_item_call)
                input("Press Enter to continue: ")
        elif inventory_item_call == "silver coin":
            if "silver coin" in inventory:
                InventoryItems.item_silver_coin(self)
            else:
                print(
                    "\n\n'%s' not in inventory.\n\n\n\n\n" %
                    inventory_item_call)
                input("Press Enter to continue: ")

    def item_notebook(self):
        self.__init__()
        item_notebook_choice = input(
            "\n\nRead or Write in 'notebook': ").lower()
        global notebook_entries
        if item_notebook_choice == "write":
            notebook_entry = input("Type what you want to write: ")
            notebook_entries.append(notebook_entry)
            print("\nEntry added to 'notebook'")
            input("\n\nPress Enter to continue: ")
        elif item_notebook_choice == "read":
            print(
                "\nThis notebook is quite old. As you open the first few "
                "pages, you come across some writing:\n\n"
                "'There was a small boy from Nantucket...'")
            print("\nYour Writing: %s\n\n" % notebook_entries)
            input("Press Enter to continue: ")
        else:
            pass

    def item_crowbar(self):
        self.__init__()
        print(
            "\n\n\nThis is the piece of metal you tripped on earlier. Maybe "
            "you can use it to get out of this place!")
        input("\n\n\n\nPress Enter to continue: ")

    def item_silver_coin(self):
        self.__init__()
        print(
            "\n\n\nA worn silver coin. Perhaps its past owner frequently "
            "used it for something.")
        input("\n\n\n\nPress Enter to continue: ")


def room_1():
    """ Room 1 is straight forward to get the player used to the outline of
    the game; 2 choices.

    Note: Each time the player 'finds' an item, they will automatically put
    the item in their inventory (global list).
          If the item is already in inventory, the game will recognise this.
          if room_1_choice_2 == '2' --> room_2()

    ITEMS: 'notebook' """
    global inventory
    while True:
        print(
            "\nEscape The House\n---------------------------\n\nInventory: "
            "%s\n" % inventory)
        print(
            "You seem to be in a room, a dark room.\n1. Feel around you\n2. "
            "Walk straight\n")
        room_1_choice_1 = input("Enter choice: ")
        if room_1_choice_1 == "1":
            if "notebook" in inventory:
                print("\n\n\nNothing is here.\n\n\n\n")
                input("Press Enter to continue: ")
            else:
                inventory.append("notebook")
                print(
                    "\n\nYou feel around you and find a notebook.\nPut "
                    "'notebook' in inventory.\n\n")
                input("\n\nPress Enter to continue: ")
        elif room_1_choice_1 == "2":
            while True:
                print(
                    "\nInventory: %s\n\nYou walk straight into a door.\n1. "
                    "Open the door\n2. Knock\n\n" % inventory)
                room_1_choice_2 = input("Enter choice: ")
                if room_1_choice_2 == "2":
                    print(
                        "\n\n\nYou knock on the door. Nothing "
                        "happens.\n\n\n\n")
                    input("Press Enter to continue: ")
                elif room_1_choice_2 == "1":
                    print(
                        "\nYou successfully open door and step through the "
                        "opening.")
                    room_2()
                elif room_1_choice_2 == "inventory" or room_1_choice_2 == "i":
                    InventoryItems().inventory_call()
                else:
                    pass
        elif room_1_choice_1 == "inventory" or room_1_choice_1 == "i":
            InventoryItems().inventory_call()
        else:
            pass


def room_2():
    """ Room 2 is more complicated as it requires the player to decode 4
    symbols. At this point, the player may have
    'notebook' in their inventory and can write the symbols in it. If they
    do, they should recognize that the symbols
    correspond to certain numbers and the numbers are for the 4-digit code
    --> room_3() (see comment below).

    ITEMS: 'crowbar' """
    while True:
        print(
            "\nInventory: %s\n\nThis room seems to be lit by two small "
            "flames in the corner.\n"
            "1. Walk over to the flame\n2. Walk away from the flame\n3. "
            "Explore the room.\n" % inventory)
        room_2_choice_1 = input("Enter choice: ")
        if room_2_choice_1 == "1":
            # The 'strange carvings' here represent numbers on a standard
            # keyboard (@ = 2, ^ = 6, $ = 4, ) = 0)
            print(
                "\nInventory: %s\n\nThe candle flickers. Strange carvings "
                "are etched into a desk:"
                "\n    @ ^ $ )\n\n\n" % inventory)
            input("Press Enter to continue: ")
        elif room_2_choice_1 == "2":
            print(
                "\nInventory: %s\n\nYou walk away from the flame and into "
                "another door. The door has a 4 digit-lock "
                "on it.\n" % inventory)
            room_2_code_1 = input(
                "\n\n\nENTER 4-DIGIT CODE (or press Enter to continue): ")
            if room_2_code_1 == "2640":
                print("\nSuccess! The code worked and unlocked the door.")
                room_3()
            else:
                pass
        elif room_2_choice_1 == "3":
            if "crowbar" in inventory:
                print(
                    "\n\n\nYou explore the room without tripping and find "
                    "out that nothing else is here.\n\n\n\n")
                input("Press Enter to continue: ")
            else:
                inventory.append("crowbar")
                print(
                    "\n\nYou decide to explore the room and trip on a metal "
                    "bar. Ouch!\n"
                    "Put 'crowbar' in inventory.\n\n\n\n")
                input("Press Enter to continue: ")
        elif room_2_choice_1 == "inventory" or room_2_choice_1 == "i":
            InventoryItems().inventory_call()
        else:
            pass


def room_3():
    """ Room 3 puts the user in a hallway which has many different options.
    This room is where the story of the game
    starts to be explained to the player. room_3_choice_2 == "2" --> room_4()

    ITEMS: 'silver coin' """
    while True:
        print(
            "\nInventory: %s\n\nYou step into a long hallway. The walls are "
            "decorated with\nChristmas "
            "decorations. Strange, as you remember that it is "
            "summertime...\n1. Walk down the hallway\n2. Examine "
            "the Christmas decorations\n" % inventory)
        room_3_choice_1 = input("Enter choice: ")
        if room_3_choice_1 == "1":
            while True:
                print(
                    "\nInventory: %s \n\nAs you walk down the hallway, "
                    "you notice that there is a room connected to "
                    "the hallway.\nThere are also stairs that lead down.\n1. "
                    "Go to room\n2. Go down the stairs\n" %
                    inventory)
                room_3_choice_2 = input("Enter choice: ")
                if room_3_choice_2 == "1":
                    while True:
                        print(
                            "\nInventory: %s\n\nThis room is very drafty. "
                            "Perhaps you should go back before you catch"
                            " a chill.\n1. Explore room\n2. Back to "
                            "hallway\n\n" % inventory)
                        room_3_choice_3 = input("Enter choice: ")
                        if room_3_choice_3 == "1":
                            if 'silver coin' in inventory:
                                print(
                                    "\n\nYou explore the room and find "
                                    "nothing else.\n\n\n\n\n")
                                input("Press Enter to continue: ")
                            else:
                                inventory.append('silver coin')
                                print(
                                    "\n\nYou explore the room and find a "
                                    "silver coin.")
                                print(
                                    "Put 'silver coin' in inventory.\n\n\n\n")
                                input("Press Enter to continue: ")
                        elif room_3_choice_3 == "inventory" or \
                                        room_3_choice_3 == "i":
                            InventoryItems().inventory_call()
                        else:
                            room_3()
                elif room_3_choice_2 == "2":
                    print(
                        "\nThe stairs are old and creak underneath your feet "
                        "as you pass.")
                    room_4()
                elif room_3_choice_2 == "inventory" or room_3_choice_2 == "i":
                    InventoryItems().inventory_call()
                else:
                    pass
        elif room_3_choice_1 == "2":
            print(
                "\n\nThe Christmas decorations all feature the same photo of "
                "a family. As you examine the decor more "
                "closely\nyou notice that one of the photos features the "
                "same family, but with an additional man"
                "\nwearing a dark brown coat and a silver coin in his "
                "hand.\n\n\n")
            input("Press Enter to continue: ")
        elif room_3_choice_1 == "inventory" or room_3_choice_1 == "i":
            InventoryItems().inventory_call()
        else:
            pass


def room_4():
    """ Room 4 is the most complicated code this game has. This is the room
    where the player can escape, and the first
    time that the player can die. The console prints differently if certain
    items are in 'inventory'. The door to win
    the game is locked and boarded up and so the player needs 'crowbar' and
    'key' to open it. When the two items are in
    'inventory', the player then breaks the boards and unlocks the door.
    When done, the console prints out a 3rd option
    to open the door --> win_game()

    ITEMS: None """
    while True:
        print(
            "Inventory: %s\n\nYou enter what seems to be a living room.\n1. "
            "Explore the living room\n2. Sit on the"
            " couch\n3. Walk towards the exit\n4. Go back upstairs\n" %
            inventory)
        room_4_choice_1 = input("Enter choice: ")
        if room_4_choice_1 == "1":
            print(
                "\n\nThis living room has not been used in years. An inch of "
                "dust covers most of the items in "
                "this\nroom. Besides the dust, there is a couch, a T.V., "
                "a table, and an old chair.\n\n\n\n")
            input("Press Enter to continue: ")
        elif room_4_choice_1 == "2":
            print(
                "\n\nAs you sit on the couch, dust plumes from the cushions! "
                "You think to yourself that suffocating\n"
                "from too much dust would be an interesting way to go "
                "out...\n\n\n\n")
            input("Press Enter to continue: ")
        elif room_4_choice_1 == "3":
            while True:
                print(
                    "\n'The exit! Yes!' You say to yourself. You walk "
                    "towards the exit.\nThe exit door is boarded "
                    "up and has a lock on it.\n1. Back to living room")
                if 'crowbar' in inventory:
                    print("2. Break the boards ('crowbar')")
                    if 'key' not in inventory:
                        input(
                            "   NOTE: Need a key to unlock the "
                            "door.\n\n\nPress Enter to continue: ")
                        room_4()
                    elif 'key' in inventory:
                        print("3. Unlock the door ('key')")
                        if 'broke_boards' and 'unlocked_door' in open_door:
                            print("4. Open the door")
                        else:
                            pass
                        room_4_choice_2 = input("\n\nEnter choice: ")
                        if room_4_choice_2 == "1":
                            room_4()
                        elif room_4_choice_2 == "2":
                            if 'broke_boards' in open_door:
                                print("\n\n\nYou already broke the boards.")
                                input("\n\n\n\nPress Enter to continue: ")
                            else:
                                open_door.append('broke_boards')
                                print("\n\n\nYou break the boards!")
                                input("\n\n\n\nPress Enter to continue: ")
                        elif room_4_choice_2 == "3":
                            if 'unlocked_door' in open_door:
                                print("\n\n\nYou already unlocked the door.")
                                input("\n\n\n\nPress Enter to continue: ")
                            else:
                                open_door.append('unlocked_door')
                                print("\n\n\nYou unlocked the door!")
                                input("\n\n\n\nPress Enter to continue: ")
                        elif room_4_choice_2 == "4":
                            if len(open_door) == 2:
                                win_game()
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                elif 'crowbar' and 'key' not in inventory:
                    input("\n\n\n\nPress Enter to continue: ")
                    room_4()
                elif 'key' in inventory:
                    print("\n3. Unlock the door ('key')")
                    input(
                        "   NOTE: Need a crowbar to break boards.\n\nPress "
                        "Enter to continue: ")
                    room_4()
                else:
                    pass
        elif room_4_choice_1 == "4":
            print(
                "\nAs you climb back up the stairs, the stairs give way. You "
                "fall to your death!")
            game_over()
        elif room_4_choice_1 == "inventory" or room_4_choice_1 == "i":
            InventoryItems().inventory_call()
        else:
            pass


def room_5():
    pass


def room_6():
    pass


def room_7():
    pass


def game_over():
    """ Game Over screen. Prints screen and brings the player back to
    MainMenu. """
    print(
        "\n          GAME OVER\n-----------------------------\n\n\nYou did "
        "not escape the house!\n\n")
    input("Press Enter to go back to Main Menu: ")
    inventory.clear()
    notebook_entries.clear()
    MainMenu.main_menu()


def win_game():
    """ Win Game screen. Prints screen and brings the player back to
    MainMenu. """
    print(
        "\n          YOU WON!\n-----------------------------\n\n\nYou "
        "successfully escaped the house!\n\n\n\n")
    input("Press Enter to go back to Main Menu: ")
    MainMenu.main_menu()


# Uncomment the two lines below to start the game from the beginning.
MainMenu = MainMenu()
MainMenu.main_menu()

room_4()
