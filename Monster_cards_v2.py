"""
Program to store monster cards for a card game
By Michael Chiu
Version 2, Component 1b: Main program while loop
12-5-26
"""

import easygui

# CONSTANTS v1
MIN_STAT = 1
MAX_STAT = 25


# catalogue dictionary v1
monster_catalogue = {
    "Stoneling" : {"Strength": 7, "Speed": 1, "Stealth": 25,"Cunning": 15},
    "Vexscream" : {"Strength": 1, "Speed": 6, "Stealth": 21,"Cunning": 19},
    "Dawnmirage" : {"Strength": 5, "Speed": 15, "Stealth": 18,"Cunning": 22},
    "Blazegolem" : {"Strength": 15, "Speed": 20, "Stealth": 23,"Cunning": 6},
    "Websnake" : {"Strength": 7, "Speed": 15, "Stealth": 10,"Cunning": 5},
    "Moldvine" : {"Strength": 21, "Speed": 18, "Stealth": 14,"Cunning": 5},
    "Vortexwing" : {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing" : {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep" : {"Strength": 14, "Speed": 14, "Stealth": 17,"Cunning": 4},
    "Wispghoul" : {"Strength": 17, "Speed": 19, "Stealth": 3,"Cunning": 2},
}

# defining stats v1
STAT_CATEGORIES = ["Strength", "Speed", "Stealth", "Cunning"]

# functions
def add_monster():
    pass

def search_edit_monster():
    pass

def delete_monster():
    pass

def print_catalogue():
    pass

# main program 
easygui.msgbox("Welcome to the Monster Card catalogue.\nMany monsters await to be unleashed!",
                "Welcome message")

# while loop v2
while True:
    option = easygui.buttonbox("What would you like to do?\n Please select from the options below:",
                                "Main menu",
                      choices = ["Add monster", "Search/Edit monster", "Delete monster", 
                                 "Print catalogue", "Exit program"])
    if option == "Add monster":
        add_monster()
        
    elif option == "Search/Edit monster":
        search_edit_monster()

    elif option == "Delete monster":
        delete_monster()

    elif option == "Print catalogue":
        print_catalogue()

    else:
        break

easygui.msgbox("Thank you for using the Monster Catalogue Program. Goodbye!"
               , "Goodbye message")
    