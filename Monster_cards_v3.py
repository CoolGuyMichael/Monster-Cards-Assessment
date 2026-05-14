"""
Program to store monster cards for a card game
By Michael Chiu
Version 3, Component 2: Add monster card function
15-5-26
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

# add monster function v3
def add_monster():
    new_name = easygui.enterbox("Please enter the name of the new monster you wish to add:",
                                "New monster name")
    
    # in case user selected 'cancel'
    if not new_name:
        return
    
    # ensure new monster is not already in catalogue
    new_name = new_name.title().strip()
    if new_name in monster_catalogue:
        easygui.msgbox(f"It seems {new_name} is already in the monster catalogue.", "Error")
        return
    
    temporary_stats = {}
    # use for loop with STAT_CATEGORIES to loop through all 4 stats
    for stat in STAT_CATEGORIES:
        value = easygui.integerbox(f"Enter the {stat} value for {new_name}:"
                                   f"\n(Must be between {MIN_STAT}-{MAX_STAT})", 
                                  f"{stat} Input", 
                                  lowerbound = MIN_STAT, 
                                  upperbound = MAX_STAT)
    
    # in case user hit 'cancel'
        if value is None:
            easygui.msgbox("Monster creation cancelled.", "Cancelled")
            return
    
        temporary_stats[stat] = value

    # confirm new monster details
    summary = f"Statistics for {new_name}:\n"
    for stat, value in temporary_stats.items():
        summary += f"- {stat}: {value}\n"
    summary += "\nAre these details correct?"

    confirmation = easygui.buttonbox(summary, "Confirm Details", choices=["Confirm", "Discard"])

    if confirmation == "Confirm":
        # add "temporary stats" to actual catalogue
        monster_catalogue[new_name] = temporary_stats
        easygui.msgbox(f"{new_name} has been added to the catalogue!", "Success")
    else:
        easygui.msgbox("Monster data discarded.\nThe new monster has not been added.", "Discarded")


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
        # temporary code to view catalogue and ensure functions like add monster and 
        # search/edit monster works properly, will be replaced in v6 for actual print function
        easygui.msgbox(f"{monster_catalogue}") 

    else:
        break

easygui.msgbox("Thank you for using the Monster Catalogue Program. Goodbye!"
               , "Goodbye message")
    